{{ if gt (len .email) 0 -}}
  "{{ .email }}" is not a valid email address.
{{ end -}}
Please enter a valid email address.