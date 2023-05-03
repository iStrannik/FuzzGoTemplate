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
func indexHandler1(w http.ResponseWriter, r *http.Request) {
	var tpl = template.Must(template.ParseFiles("../epochs_1/index.html"))
    tpl.Execute(w, nil)
}
func indexHandler3(w http.ResponseWriter, r *http.Request) {
	var tpl = template.Must(template.ParseFiles("../epochs_3/index.html"))
    tpl.Execute(w, nil)
}
func indexHandler5(w http.ResponseWriter, r *http.Request) {
	var tpl = template.Must(template.ParseFiles("../epochs_5/index.html"))
    tpl.Execute(w, nil)
}
func indexHandler7(w http.ResponseWriter, r *http.Request) {
	var tpl = template.Must(template.ParseFiles("../epochs_7/index.html"))
    tpl.Execute(w, nil)
}
func indexHandler9(w http.ResponseWriter, r *http.Request) {
	var tpl = template.Must(template.ParseFiles("../epochs_9/index.html"))
    tpl.Execute(w, nil)
}
func indexHandler11(w http.ResponseWriter, r *http.Request) {
	var tpl = template.Must(template.ParseFiles("../epochs_11/index.html"))
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
    mux.HandleFunc("/1", indexHandler1)
    mux.HandleFunc("/3", indexHandler3)
    mux.HandleFunc("/5", indexHandler5)
    mux.HandleFunc("/7", indexHandler7)
    mux.HandleFunc("/9", indexHandler9)
    mux.HandleFunc("/11", indexHandler11)
    http.ListenAndServe(":"+port, mux)
}
