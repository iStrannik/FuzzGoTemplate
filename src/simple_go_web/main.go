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
func indexHandler10(w http.ResponseWriter, r *http.Request) {
	var tpl = template.Must(template.ParseFiles("../epochs_10/index.html"))
    tpl.Execute(w, nil)
}
func indexHandler11(w http.ResponseWriter, r *http.Request) {
	var tpl = template.Must(template.ParseFiles("../epochs_11/index.html"))
    tpl.Execute(w, nil)
}
func indexHandler15(w http.ResponseWriter, r *http.Request) {
	var tpl = template.Must(template.ParseFiles("../epochs_15/index.html"))
    tpl.Execute(w, nil)
}
func indexHandler21(w http.ResponseWriter, r *http.Request) {
	var tpl = template.Must(template.ParseFiles("../epochs_21/index.html"))
    tpl.Execute(w, nil)
}
func indexHandler25(w http.ResponseWriter, r *http.Request) {
	var tpl = template.Must(template.ParseFiles("../epochs_25/index.html"))
    tpl.Execute(w, nil)
}
func indexHandler50(w http.ResponseWriter, r *http.Request) {
	var tpl = template.Must(template.ParseFiles("../epochs_50/index.html"))
    tpl.Execute(w, nil)
}
func indexHandler75(w http.ResponseWriter, r *http.Request) {
	var tpl = template.Must(template.ParseFiles("../epochs_75/index.html"))
    tpl.Execute(w, nil)
}
func indexHandler100(w http.ResponseWriter, r *http.Request) {
	var tpl = template.Must(template.ParseFiles("../epochs_100/index.html"))
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

    fs := http.FileServer(http.Dir("../"))
    http.Handle("/", http.StripPrefix("/", fs))
    /*
    mux := http.NewServeMux()

    mux.HandleFunc("/kek", kekHandler)
    mux.HandleFunc("/1", indexHandler1)
    mux.HandleFunc("/3", indexHandler3)
    mux.HandleFunc("/5", indexHandler5)
    mux.HandleFunc("/7", indexHandler7)
    mux.HandleFunc("/9", indexHandler9)
    mux.HandleFunc("/10", indexHandler10)
    mux.HandleFunc("/11", indexHandler11)
    mux.HandleFunc("/15", indexHandler15)
    mux.HandleFunc("/21", indexHandler21)
    mux.HandleFunc("/25", indexHandler25)
    mux.HandleFunc("/50", indexHandler50)
    mux.HandleFunc("/75", indexHandler75)
    mux.HandleFunc("/100", indexHandler100)
    mux.HandleFunc("/", indexHandler)
    */
    http.ListenAndServe(":"+port, nil)
}
