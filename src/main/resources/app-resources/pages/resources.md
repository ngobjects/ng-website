# Resources

## Where files go

In `src/main/resources`:

| Folder | Used for | Served at |
| --- | --- | --- |
| `webserver-resources` | CSS, JS, images | `/nr/app/…` |
| `public` | `favicon.ico`, `robots.txt`, … | `/…` (site root) |
| `app-resources` | Files your code reads, `Properties` | Not served |
| `components` | Templates | Not served |

## In templates

```html
<wo:stylesheet filename="main.css" />
<wo:script filename="app.js" />
<wo:img filename="logo.png" alt="Logo" />
```

Paths are relative to `webserver-resources`. `<wo:resourceURL filename="…" />` renders just the URL. Add `namespace="…"` for a [plugin](plugins)'s resources; the default is `app`.

Generated images:

```html
<wo:img data="$chartBytes" mimeType="image/png" />
```

These are served once, from `/nd/…`.

## In Java

```java
final byte[] bytes = application().resourceManager()
		.obtainAppResource( "app", "countries.csv" )
		.orElseThrow()
		.bytes();
```

Also `obtainWebserverResource` and `obtainPublicResource`.

*(TODO: streaming large resources, [#40](https://github.com/ngobjects/ng-objects/issues/40).)*
