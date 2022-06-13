# Templating

Templates in ng-objects usually consist of a plain HTML-file and an associated Java class (which must inherit from NGComponent).\
The template (HTML-file for our example) allows you to add ```dynamic tags``` with ```bindings``` that can link to values from the associated Java class.\


### Example

#### HTML-file

```html
<body>
	<wo:str value="$someString" />
</body>
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


## Dynamic tags

(TODO: Add an example image)

A dynamic tag always starts with ```<wo:``` followed by a ```tag identifier``` and then an optional list of ```bindings```.\
Dynamic tags must always be "closed", i.e. if they have no associated closing tag, you must end the "opening" tag with ```/>```

 ```<wo:tagIdentifier binding1="$someVariable" binding2="SomeConstant" />```.

* **tagIdentifier**\
identifies which dynamic tag to use. This can be a fully qualified class name ```(ng.appserver.elements.NGString)```, the simple class name ```(NGString)``` or a shortcut provided for the tag ```(str)```

* **$someVariable**\
Bindings whose value starts with a ```$``` are dynamic and resolved against the java template. The identifier passed to the binding can be either a field name or a method name. The mechanics of the resolution are actually more advanced (see KeyValueCoding TODO).

* **SomeConstant**\
Bindings whose value does not start with a ```$``` are constant. Constant values can be a String, Integer or a Double. There is one exception from this rule; if you want to pass in a boolean constant, you use ```$true``` and  ```$false```.

#### Acknowledgements and thanks

The template parser in ng-objects is ripped off from the Woognl template parser in [Project Wonder](https://github.com/wocommunity/wonder), although without the "ognl"-part. Awesome work mostly created by Mike Schrag and maintained and improved by the WOCommunity. Lots of thanks to him and all the others!