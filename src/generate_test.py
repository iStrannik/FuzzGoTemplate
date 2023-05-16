import itertools
import subprocess
import uuid
import random
from os import getcwd
from os.path import join
import os


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
        if key not in oldreport or (int(oldreport[key][1]) == 0 and int(newreport[key][1]) != 0):
            result = True
        if key not in oldreport or int(newreport[key][1]) > int(oldreport[key][1]):
            oldreport[key] = value
    return oldreport, result


def generate_test(template, Range_data, B_data, C_data, random_string):
    Range_data = ','.join(Range_data)
    a = '''
    package template
    import (
        // "strings"
        "fmt"
        "testing"
        // "io/ioutil"
        "os"
        // "reflect"
    )

    func random_string() string {
        return ''' + random_string + '''
    }

    func TestKek(t *testing.T) {
        _ = os.Remove("./prepared.html")
        f, err := os.OpenFile("./prepared.html", os.O_CREATE | os.O_WRONLY, 0777)
        if err != nil {
            fmt.Println(err)
            return
        }
        defer f.Close()
        test_input := `''' + template + '''`
        data := struct {
            A []string
            B string
            C string
            D struct {
                A []string
                B string
                C string
            }
            E int
            F int
            print func(a any) any
            random_string func() string
        }{
            A: []string{''' + Range_data + '''},
            B: ''' + B_data + ''',
            C: ''' + C_data + ''',
            D: struct {
                A []string
                B string
                C string
            }{
                A: []string{''' + Range_data + '''},
                B: ''' + B_data + ''',
                C: ''' + C_data + ''',
            },
            E: 5,
            F: 7,
            print: print,
            random_string: random_string,
        }
        tmpl := New("foo").Funcs(FuncMap{
            "print" : print,
            "random_string" : random_string,
        })
        tmpl = Must(tmpl.Parse(test_input))
        // b := new(strings.Builder)
        if err := tmpl.Execute(f, data); err != nil {
            t.Errorf("%v", err)
        }
    }

    func print(a any) any {
        return a
    }
    '''
    return a


def subsets(data):
    return itertools.chain.from_iterable(itertools.combinations_with_replacement(data, r) for r in range(len(data) + 1))


def get_coverage(template,
                 package,
                 coverpkg=['.', 'text/template'],
                 oldcoverage={},
                 success_path='./epochs/possible_xss'):

    with open(template, 'r') as file:
        template_data = file.read().replace('\n', '')

    updatedcoverage = oldcoverage
    data = [
        "` <script>alert('you have been pwned')</script> `", "` <img src/onerror=alert(1)> `", "` onerror=alert(1) `",
        "` <is-custom onload='alert(1)' super-custom='test' /> `", "`javascript:alert`", "` <svg onload=alert(1)> `"
    ]
    findNewCow = False

    for i in range(8):
        with open(package + '/kek_test.go', 'w') as file:
            code = generate_test(template_data, [random.choice(data) for _ in range(random.randint(1, 4))],
                                 random.choice(data), random.choice(data), random.choice(data))
            file.write(code)
        for pkg in coverpkg:
            a = subprocess.Popen([
                "go", "test", "-coverprofile",
                join(getcwd(), "report.txt"), "-covermode", "count", "-coverpkg", pkg, "."
            ],
                                 cwd=package)
            _ = a.wait()
            b = subprocess.Popen(['node', 'detect_alerts/detect_alert.js'],
                                 stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE)
            b.stdin.write((package + '/prepared.html' + '\n').encode())
            b.stdin.close()
            ans = b.stdout.readline()
            if b'pwned_succesfull' in ans:
                with open(template, 'r') as file:
                    success_data = file.read()
                template_name = str(uuid.uuid4())
                with open(join(success_path, template_name + '.tpl'), 'w') as file:
                    file.write(success_data)
                with open(join(success_path, template_name + '.go'), 'w') as file:
                    file.write(code)
                os.rename(package + '/prepared.html', join(success_path, template_name + '.html'))
            newcoverage = parse_report_file("report.txt")
            updatedcoverage, res = merge_reports(updatedcoverage, newcoverage)
            if res:
                findNewCow = True
                print(f'Find new coverage with data {i}')
    a = subprocess.Popen([
            "go", "clean", "-cache"
        ], cwd=package)
    _ = a.wait()

    return findNewCow, updatedcoverage


# print(get_coverage('../official_test_templates/file2.tpl',
#      '/home/strannik/go/src/go/src/html/template'))
