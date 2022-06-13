# Templating

Templates in ng-objects consist of a Java class (which must inherit from NGComponent) and an associated HTML-file.

The template language as such is really just plain HTML, but you can sprinkle in "dynamic tags" that link to the associated Java class.
A dynamic tag always looks like ```<wo:[tagname] binding1="$[someVariable]" binding2="SomeConstant" />```.

(TODO: Add an example image)

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

#### Acknowledgements and thanks

The template parser in ng-objects is ripped off from the Woognl template parser in [Project Wonder](https://github.com/wocommunity/wonder), awesome work mostly created by Mike Schrag. Lots of thanks to him and the rest of the community!