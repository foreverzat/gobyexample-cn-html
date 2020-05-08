package main

import (
	"fmt"
	"os"
	"net/http"
	"path/filepath"
	"path"
)
type fileHandler struct {
    root http.FileSystem
    h    http.Handler
}

func fileServer(root http.FileSystem, h http.Handler) http.Handler {
    return &fileHandler{root, h}
}

func (f *fileHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	root, _ := os.Getwd()
	path := path.Join(root, r.URL.Path)
    if _, err := os.Stat(path); os.IsNotExist(err) {
		if ext := filepath.Ext(path); ext == "" {
			r.URL.Path += ".html"
		} else {
			http.ServeFile(w, r, "404.html")
			return
		}
	}
    f.h.ServeHTTP(w, r)
}

func main() {
	port := ":8000"
    fmt.Printf("Serving at: http://localhost%s\n", port)
	fs := http.Dir("")
	http.Handle("/", fileServer(&fs, http.FileServer(&fs)))
	// http.Handle("/", http.FileServer(fs))
    http.ListenAndServe(port, nil)
}