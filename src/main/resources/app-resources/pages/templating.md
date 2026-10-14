| ❤️ **Acknowledgements**\
The template parser is Project Wonder's *WOOgnl* parser, created by Mike Schrag and improved by the WOCommunity. Huge thanks to Mike and everyone who contributed.

# Templating

A component's template is HTML plus dynamic tags. Bindings on the tags connect to the component's Java class.

```html
<p>Hello <wo:str value="$name" />!</p>
```

```java
public class Hello extends NGComponent {

	public String name = "world";

	public Hello( NGContext context ) {
		super( context );
	}
}
```

## Template files

In `src/main/resources/components`, named after the class:

* `Hello.html`, or
* `Hello.wo/Hello.html` (plus an optional `Hello.wod`)

No subfolders. A template without a class works too.

## Dynamic tags

```html
<wo:tagName binding1="$someKey" binding2="Some constant" />
```

* Always close the tag: `</wo:tagName>`, or `/>`.
* The tag name is a short name (`str`), a simple class name (`NGString`, `Hello`) or a fully qualified one.

All built-in elements: [Dynamic elements](dynamic-elements).

## Binding values

| Value | Meaning |
| --- | --- |
| `$name`, `$user.name` | Key or keypath, resolved with [KeyValueCoding](key-value-coding) |
| `Some text` | Constant string. Escapes: `\n \r \t \\ \" \$` |
| `$true`, `$false` | Boolean constants |
| `$42`, `$1.5` | Integer and Double constants |
| *(no value)* `<wo:link disabled>` | `true` |
| `$^name` | The value the parent bound to this component's `name` binding |

No WebObjects `@` operators, and no binding twice on one tag.

## Embedding components

```html
<wo:Hello name="$user.firstName" />
```

A wrapper renders the content between its tags at `<wo:content />`:

```html
<!-- Page.html -->
<body>
	<header>My site</header>
	<wo:content />
</body>
```

```html
<wo:Page>
	<p>Inside the body, below the header.</p>
</wo:Page>
```

## WOD files

Supported, for templates coming from WebObjects:

```html
<webobject name="Greeting" />
```

```
Greeting : NGString {
	value = name;
}
```

Quoted values are constants, unquoted ones keypaths. Use engifer's element names (`NGString` or `str`), not `WOString`.

## Directives

* `<p:raw>…</p:raw>`: output as is, no dynamic tags.
* `<p:comment>…</p:comment>`: left out of the output.
