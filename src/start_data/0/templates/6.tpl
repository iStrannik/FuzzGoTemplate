{{ template "header.tmpl" "Index" }}

<section>
{{ range $post := . }}
{{ template "post.tmpl" $post }}
{{ end }}
</section>

{{ template "footer.tmpl" }}