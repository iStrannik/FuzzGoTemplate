
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
        return ` <img src/onerror=alert(1)> `
    }

    func TestKek(t *testing.T) {
        _ = os.Remove("./prepared.html")
        f, err := os.OpenFile("./prepared.html", os.O_CREATE | os.O_WRONLY, 0777)
        if err != nil {
            fmt.Println(err)
            return
        }
        defer f.Close()
        test_input := `<br>{{.C }}</br><img src=xx:{{.LocalName }}>`
        data := struct {
            A []string
            B string
            C string
            D struct {
                A []string
                B string
                C string
            }
            print func(a any) any
            random_string func() string
        }{
            A: []string{` <svg onload=alert(1)> `,` <is-custom onload='alert(1)' super-custom='test' /> `,`javascript:alert`},
            B: ` <svg onload=alert(1)> `,
            C: ` <script>alert('you have been pwned')</script> `,
            D: struct {
                A []string
                B string
                C string
            }{
                A: []string{` <svg onload=alert(1)> `,` <is-custom onload='alert(1)' super-custom='test' /> `,`javascript:alert`},
                B: ` <svg onload=alert(1)> `,
                C: ` <script>alert('you have been pwned')</script> `,
            },
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
    