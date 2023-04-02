{{ define "header" -}}
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <meta http-equiv="cache-control" content="max-age=0" />
  <meta http-equiv="cache-control" content="no-cache" />
  <meta http-equiv="expires" content="0" />
  <meta http-equiv="expires" content="Tue, 01 Jan 1980 1:00:00 GMT" />
  <meta http-equiv="pragma" content="no-cache" />
  <title>{{ .title }}</title>
</head>
<body>
<header>
  <nav><ul>
    {{/* We know if a user is logged in or not. */}}
    {{ if .user }}
    <li>Logged in as {{ .user.GetEmail }}</li>
    <li><form action="{{ .config.RouteLogOut }}" method="post"><button>Log out</button></form></li>
    {{ else }}
    <li><a href="{{ .config.RouteLogIn }}">Log in</a></li>
    <li><a href="{{ .config.RouteSignUp }}">Sign up</a></li>
    {{ end }}
  </ul></nav>
</header>
<main>
{{ end }}