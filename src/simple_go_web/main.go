package main

import (
    "html/template"
    "net/http"
    "os"
)

func indexHandler(w http.ResponseWriter, r *http.Request) {
	var tpl = template.Must(template.ParseFiles("../index.html"))
    tpl.Execute(w, nil)
}

func main() {
    port := os.Getenv("PORT")
    if port == "" {
        port = "1337"
    }

    mux := http.NewServeMux()

    mux.HandleFunc("/", indexHandler)
    http.ListenAndServe(":"+port, mux)
}