import itertools
import subprocess
from os import getcwd
from os.path import join


def parse_report_file(filename):
    result = {}
    with open(filename, 'r') as file:
        for i in file.readlines()[1:]:
            a = i.split(' ')
            if int(a[2]) > 0:
                result[a[0]] = 1
    return result


def merge_reports(oldreport, newreport):
    result = False
    for key, _ in newreport.items():
        if key not in oldreport:
            result = True
            oldreport[key] = 1
    return oldreport, result


def generate_test(template, data):
    data = ','.join(data)
    a = '''
    package template
    import (
        "strings"
        "testing"
    )
    func TestKek(t *testing.T) {
        test_input := "''' + template + '''"
        tmpl := New("foo")
        tmpl = Must(tmpl.Parse(test_input))
        b := new(strings.Builder)
        if err := tmpl.Execute(b,''' + data + ''' ); err != nil {
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
            "`<img src/onerror=prompt(8)>`"]
    findNewCow = False
    canRun = False

    for i in subsets(data):
        with open(package + '/kek_test.go', 'w') as file:
            file.write(generate_test(template_data, i))
        for pkg in coverpkg:
            a = subprocess.Popen(
                ["go", "test", "-coverprofile", join(getcwd(), "report.txt"), "-coverpkg", pkg, "."], cwd=package)
            err = a.wait()
            if err != 0:
                canRun = True
                continue
            newcoverage = parse_report_file("report.txt")
            updatedcoverage, res = merge_reports(updatedcoverage, newcoverage)
            if res:
                findNewCow = True
                print(f'Find new coverage with data {i}')

    return canRun, findNewCow, updatedcoverage


# print(get_coverage('../official_test_templates/file2.tpl',
#      '/home/strannik/go/src/go/src/html/template'))
