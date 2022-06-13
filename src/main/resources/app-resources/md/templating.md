# Templating

Templates in ng-objects consist of a Java class (which must inherit from NGComponent) and an associated HTML-file.

The template language as such is just plain HTML, but you can sprinkle in "dynamic tags" that allow you to show content from the templates class.

### Example

#### HTML-file

```html
[...]
<body>
	<wo:str value="$someString" />
</body>
[...}
```

#### Associated java class

```java
public class MyComponent extends NGComponent {

	public String someString = "Hello world";

	public MyComponent( NGContext context ) {
		super( context );
	}
}
```

