package main

import (
    "net/http"
    "os"
)

func main() {
    port := os.Getenv("PORT")
    if port == "" {
        port = "1337"
    }

    fs := http.FileServer(http.Dir("/fuzzer/"))
    http.Handle("/", http.StripPrefix("/", fs))
    http.ListenAndServe(":"+port, nil)
}
