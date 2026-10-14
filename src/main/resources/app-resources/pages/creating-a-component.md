# Creating a component

A Java class and a template with the same name.

## 1. The class

In your app's package or its `components` subpackage:

```java
public class ProductCard extends NGComponent {

	public Product product;

	public ProductCard( NGContext context ) {
		super( context );
	}

	public boolean onSale() {
		return product.discount() > 0;
	}
}
```

## 2. The template

`src/main/resources/components/ProductCard.html`:

```html
<div class="card">
	<h3><wo:str value="$product.name" /></h3>
	<wo:if condition="$onSale"><span class="sale">Sale!</span></wo:if>
</div>
```

## 3. Use it

```html
<wo:repetition list="$products" item="$currentProduct">
	<wo:ProductCard product="$currentProduct" />
</wo:repetition>
```

## Bindings

By default, each binding is copied into the public field or setter of the same name (`product` above), and copied back afterwards. Every binding needs one.

To read bindings yourself instead:

```java
@Override
public boolean synchronizesVariablesWithBindings() {
	return false;
}

public Product product() {
	return (Product)valueForBinding( "product" );
}
```

Also: `hasBinding( "name" )`, `setValueForBinding( value, "name" )`, and `$^name` in the template.

## As a page

```java
public NGActionResults showProduct() {
	final ProductPage page = pageWithName( ProductPage.class );
	page.product = product;
	return page;
}
```

Or map it to a URL with a [route](routing).

## As a wrapper

Put `<wo:content />` where the wrapped content goes. See [Templating](templating#embedding-components).
