{{ template "header" title . "Log in" -}}

<h1>Log in</h1>

{{ if .error }}<p class="error">{{ .error }}</p>{{ end -}}

<form action="{{ .config.RouteLogIn }}" method="post">
  <ul>
    <li><label for="email">Email:</label>
      <input type="email" id="email" name="email" required autofocus tabindex="10"/></li>
    <li><label for="password">Password:</label>
      <input type="password" id="password" name="password" autocomplete="current-password" minlength="8" required tabindex="20"/></li>
    <li><button type="submit" tabindex="30">Log in</button></li>
  </ul>
</form>

<p><a href="{{ .config.RouteForgottenPassword }}">Forgot your password?</a></p>

{{- template "footer" . }}