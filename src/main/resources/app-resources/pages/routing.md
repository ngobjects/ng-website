# Routing

| 🚧 **Being redesigned**\
Typed routes are on the way. The API below works today, but will change.

Routes map URLs to pages and functions. They're stateless: use them for anything that needs a stable URL.

```java
@Override
public Routes routes() {
	return super.routes()
			.map( "/", FrontPage.class )
			.map( "/hello", () -> NGResponses.ok( "Hello!" ) )
			.map( "/products/*", this::productPage );
}

private NGActionResults productPage( NGRequest request ) {
	final String id = request.uri().substring( "/products/".length() );
	...
}
```

## Targets

| Target | |
| --- | --- |
| Component class | A new page instance per request |
| `NGRequest -> NGActionResults` | When you need the request |
| `() -> NGActionResults` | When you don't |
| `NGRequestHandler` | Full control |

## Matching

* Exact, or a prefix when the path ends with `*`.
* No named parameters (`/products/:id`) yet ([#17](https://github.com/ngobjects/ng-objects/issues/17)), and no matching on the HTTP method.
* Your routes win over the framework's, so mapping `/` replaces the welcome page.
* If nothing matches, a file in `src/main/resources/public` with that path is served, otherwise a 404.
* In development, routes are re-read on every request.

## Reserved prefixes

| Prefix | |
| --- | --- |
| `/no/` | [Component actions](component-actions) |
| `/na/` | [Direct actions](glossary#direct-action) |
| `/nr/` | [Resources](resources) |
| `/nd/` | Dynamic resources |
| `/ng/` | Framework and [development tools](development-tools) |
