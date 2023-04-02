{{ template "header" title . "Sign up" -}}

<h1>Sign up</h1>

{{ if .error }}<p class="error">{{ .error }}</p>{{ end -}}

<form action="{{ .config.RouteSignUp }}" method="post">
  <ul>
    <li><label for="email">Email:</label>
      <input type="email" {{ if and .infos .infos.email }}value="{{ .infos.email }}"{{ end -}} id="email" name="email" required autofocus tabindex="10"/></li>
    <li><label for="password">Password:</label>
      <input type="password" id="password" name="password" autocomplete="new-password" minlength="8" required tabindex="20"/></li>
    <li><label for="passwordconfirm">Confirm password:</label>
      <input type="password" id="passwordconfirm" name="passwordconfirm" autocomplete="new-password" minlength="8" required tabindex="30" oninput="this.setCustomValidity(document.getElementById('password').value !== this.value ? 'Please enter a matching password' : '')"/></li>
    <li><button type="submit" tabindex="40">Create new account</button></li>
  </ul>
</form>

{{- template "footer" . }}