<div class="navbar bg-base-200">
  <div class="flex-1">
    <a class="btn btn-ghost normal-case text-xl" href="/">{{ .name }}</a>
  </div>
  <div class="flex-none hidden md:block">
    <ul class="menu menu-horizontal p-0">
      {{ if .currentUser.Admin }}
        <div class="flex">
          <li><a href="/products">Products</a></li>
          <li><a href="/products/create">Add Product</a></li>
        </div>
      {{ end}}  
      {{ if .currentUser.Anon  }}
      <li><a href="/users/login">Login</a></li>
      {{ else }}
      <li><a href="/users/logout" method="post">Logout</a></li>
      {{ end }}
    </ul>
  </div>
  <div id="burger" class="px-4 cursor-pointer md:hidden">
    <svg class="w-6"xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
      <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
    </svg>        
  </div>
</div>
<div class="flex justify-end">
  <ul id="menu" class="hidden menu bg-base-200">
    {{ if .currentUser.Admin }}
        <li><a href="/products">Products</a></li>
        <li><a href="/products/create">Add Product</a></li>
    {{ end}}  
    {{ if .currentUser.Anon  }}
    <li><a href="/users/login">Login</a></li>
    {{ else }}
    <li><a href="/users/logout" method="post">Logout</a></li>
    {{ end }}
  </ul>     
</div>