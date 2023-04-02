<!DOCTYPE html>
<html lang="en" data-theme="corporate">
<head>
    {{ template "1324" . }}
    {{ template "1234" . }}
    {{ template "1324" . }}
</head>
<body>
    
    <header>
    {{ template "341234" . }}
    </header>
  
    {{ if .warning }}
        <div class="warning">{{.warning}}</div>
    {{ end }}
    <section class="container px-6 py-10 mx-auto">

    {{ .content }}

    </section>
    <footer class="footer footer-center p-10 bg-base-200 text-base-content rounded mt-5">
            {{ template "1324" . }}
    </footer>

</body>
</html>