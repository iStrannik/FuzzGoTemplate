
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
        return `javascript:alert`
    }

    func TestKek(t *testing.T) {
        f, err := os.OpenFile("./prepared.html", os.O_CREATE | os.O_WRONLY, 0777)
        if err != nil {
            fmt.Println(err)
            return
        }
        defer f.Close()
        test_input := `{{.C }}TEXT{{.A }}{{.A }}{{ if .C }}<script>{{.C }}</script>{{end}}TEXT<script>{{.D }}</script><img src=xx:{{ if .LocalName }}{{ if .B }}{{ if .C }}{{.B }}{{end}}{{end}}{{end}}>`
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
            A: []string{` <script>alert('you have been pwned')</script> `},
            B: ` <img src/onerror=alert(1)> `,
            C: ` <img src/onerror=alert(1)> `,
            D: struct {
                A []string
                B string
                C string
            }{
                A: []string{` <script>alert('you have been pwned')</script> `},
                B: ` <img src/onerror=alert(1)> `,
                C: ` <img src/onerror=alert(1)> `,
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
    