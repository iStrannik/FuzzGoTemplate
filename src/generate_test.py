import itertools
import subprocess
from os import getcwd
from os.path import join


def parse_report_file(filename):
    result = {}
    with open(filename, 'r') as file:
        for i in file.readlines()[1:]:
            a = i.split(' ')
            result[a[0]] = (a[1], a[2])
    return result


def merge_reports(oldreport, newreport):
    result = False
    for key, value in newreport.items():
        if key not in oldreport or newreport[key][1] > oldreport[key][1]:
            result = True
            oldreport[key] = value
    return oldreport, result


def generate_test(template, data):
    #data = ','.join(data)
    a = '''
    package template
    import (
        // "strings"
        "fmt"
        "testing"
        // "io/ioutil"
        "os"
    )
    func TestKek(t *testing.T) {
        f, err := os.OpenFile("./prepared.html", os.O_CREATE | os.O_WRONLY, 0777)
        if err != nil {
            fmt.Println(err)
            return
        }
        defer f.Close()
        test_input := `''' + template + '''`
        data := struct {
            A []string
        }{
            A: []string{''' + data + '''},
        }
        tmpl := New("foo")
        tmpl = Must(tmpl.Parse(test_input))
        // b := new(strings.Builder)
        if err := tmpl.Execute(f, data); err != nil {
            t.Errorf("%v", err)
        }
    }
    '''
    return a


def subsets(data):
    return itertools.chain.from_iterable(itertools.combinations_with_replacement(data, r) for r in range(len(data)+1))


def get_coverage(template, package, coverpkg=['.', 'text/template'], oldcoverage={}):

    with open(template, 'r') as file:
        template_data = file.read().replace('\n', '')

    updatedcoverage = oldcoverage
    data = ["`<script>alert('you have been pwned')</script>`",
            "`<img src/onerror=alert(1)>`",
            "onerror=alert(1)",
            "<is-custom onload='alert(1)' super-custom='test' />",
            "javascript:alert",
            "<svg onload=alert(1)>"]
    findNewCow = False

    for i in data:
        with open(package + '/kek_test.go', 'w') as file:
            file.write(generate_test(template_data, i))
        for pkg in coverpkg:
            a = subprocess.Popen(
                ["go", "test", "-coverprofile", join(getcwd(), "report.txt"), "-covermode", "count", "-coverpkg", pkg, "."], cwd=package)
            err = a.wait()
            if err != 0:
                b = subprocess.Popen(['node', 'detect_alerts/detect_alert.js'], stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE)
                b.stdin.write((package + '/prepared.html').encode())
                b.stdin.close()
                ans = b.stdout.readline()
                if b'pwned_succesfull' in ans:
                    print(f'temaplate {template} pwned!!!!!!!!!!!!!')
            newcoverage = parse_report_file("report.txt")
            updatedcoverage, res = merge_reports(updatedcoverage, newcoverage)
            if res:
                findNewCow = True
                print(f'Find new coverage with data {i}')

    return findNewCow, updatedcoverage


# print(get_coverage('../official_test_templates/file2.tpl',
#      '/home/strannik/go/src/go/src/html/template'))
