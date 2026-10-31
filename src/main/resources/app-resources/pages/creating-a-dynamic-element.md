# Creating a dynamic element

Dynamic elements are stateless: one instance serves every render of a template. Keep bindings in fields set by the constructor, and nothing else. Need state? Write a [component](creating-a-component).

## A simple element

```java
public class Copyright extends NGDynamicElement {

	public Copyright( String name, Map<String, NGAssociation> associations, NGElement contentTemplate ) {
		super( name, associations, contentTemplate );
	}

	@Override
	public void appendToResponse( NGResponse response, NGContext context ) {
		response.appendContentString( "© " + Year.now().getValue() );
	}
}
```

### Usage

```html
<wo:Copyright />
```

Put the class in your app's package or its `components` subpackage, and use it by its simple class name.

## With a binding

Bindings arrive in the constructor's `associations`. Here `since` is optional, so the element works with it and without it:

```java
public class Copyright extends NGDynamicElement {

	private final NGAssociation _since;

	public Copyright( String name, Map<String, NGAssociation> associations, NGElement contentTemplate ) {
		super( name, associations, contentTemplate );
		_since = associations.get( "since" );
	}

	@Override
	public void appendToResponse( NGResponse response, NGContext context ) {
		response.appendContentString( "© " );

		if( _since != null ) {
			response.appendContentString( _since.valueInComponent( context.component() ) + "–" );
		}

		response.appendContentString( String.valueOf( Year.now().getValue() ) );
	}
}
```

### Usage

```html
<wo:Copyright since="2019" />
```

* Read values with `association.valueInComponent( context.component() )`, and set them with `setValue( value, component )`.
* For a missing required binding, throw `NGBindingConfigurationException` from the constructor. It shows as an error box in the page.

## With content

To render content between the tags, extend `NGDynamicGroup` instead, and call `appendChildrenToResponse( response, context )` where the content goes:

```java
public class Copyright extends NGDynamicGroup {

	private final NGAssociation _since;

	public Copyright( String name, Map<String, NGAssociation> associations, NGElement contentTemplate ) {
		super( name, associations, contentTemplate );
		_since = associations.get( "since" );
	}

	@Override
	public void appendToResponse( NGResponse response, NGContext context ) {
		response.appendContentString( "© " );

		if( _since != null ) {
			response.appendContentString( _since.valueInComponent( context.component() ) + "–" );
		}

		response.appendContentString( Year.now().getValue() + " " );
		appendChildrenToResponse( response, context );
	}
}
```

### Usage

```html
<wo:Copyright since="2019">Hugi Thordarson</wo:Copyright>
```

## Actions and forms

Override `takeValuesFromRequest` and `invokeAction` too, as `NGHyperlink` and `NGTextField` do. Groups pass them on with `takeChildrenValuesFromRequest` and `invokeChildrenAction`. *(TODO: example.)*
