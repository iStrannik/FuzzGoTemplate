{{ template "header" title . "Account verified" -}}

<h1>Your account has been verified</h1>

<p><a href="{{ .config.RouteLogIn }}">Click here</a> to log in.</p>

{{- template "footer" . }}