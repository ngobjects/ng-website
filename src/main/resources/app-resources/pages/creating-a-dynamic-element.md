# Creating a dynamic element

Dynamic elements are stateless: one instance serves every render of a template. Keep bindings in fields set by the constructor, and nothing else. Need state? Write a [component](creating-a-component).

## A simple element

```java
public class CurrentYear extends NGDynamicElement {

	public CurrentYear( String name, Map<String, NGAssociation> associations, NGElement contentTemplate ) {
		super( null, null, null );
	}

	@Override
	public void appendToResponse( NGResponse response, NGContext context ) {
		response.appendContentString( String.valueOf( Year.now().getValue() ) );
	}
}
```

```html
&copy; <wo:CurrentYear />
```

* The constructor signature is required, and it must call `super( null, null, null )`.
* Put the class in your app's package or its `components` subpackage, and use it by its simple class name.

## With bindings and content

Extend `NGDynamicGroup` to render content between the tags:

```java
public class Note extends NGDynamicGroup {

	private final NGAssociation _important;

	public Note( String name, Map<String, NGAssociation> associations, NGElement contentTemplate ) {
		super( name, associations, contentTemplate );
		_important = associations.get( "important" );
	}

	@Override
	public void appendToResponse( NGResponse response, NGContext context ) {
		final boolean important = _important != null
				&& _important.booleanValueInComponent( context.component() );

		response.appendContentString( important ? "<aside class=\"note important\">" : "<aside class=\"note\">" );
		appendChildrenToResponse( response, context );
		response.appendContentString( "</aside>" );
	}
}
```

```html
<wo:Note important="$true">Back up first.</wo:Note>
```

* Read values with `association.valueInComponent( context.component() )`, and set them with `setValue( value, component )`.
* For a missing required binding, throw `NGBindingConfigurationException` from the constructor. It shows as an error box in the page.
* Truthiness: only `null`, `false` and `0` are false.

## Actions and forms

Override `takeValuesFromRequest` and `invokeAction` too, as `NGHyperlink` and `NGTextField` do. Groups pass them on with `takeChildrenValuesFromRequest` and `invokeChildrenAction`. *(TODO: example.)*
