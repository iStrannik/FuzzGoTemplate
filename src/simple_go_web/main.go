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

func kekHandler(w http.ResponseWriter, r *http.Request) {
	var tpl = template.Must(template.ParseFiles("./With_mutation_update.html"))
    tpl.Execute(w, nil)
}

func main() {
    port := os.Getenv("PORT")
    if port == "" {
        port = "1337"
    }

    mux := http.NewServeMux()

    mux.HandleFunc("/kek", kekHandler)
    mux.HandleFunc("/", indexHandler)
    http.ListenAndServe(":"+port, mux)
}