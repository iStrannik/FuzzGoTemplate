{{ template "1" "Index" }}

<section>
{{ range $post := . }}
{{ template "post.tmpl" $post }}
{{ end }}
</section>

{{ template "footer.tmpl" }}