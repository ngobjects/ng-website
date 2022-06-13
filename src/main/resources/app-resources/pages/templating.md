# Templating

Templates in ng-objects usually consist of a plain HTML-file and an associated Java class (which must inherit from NGComponent). The template allows you to add ```dynamic tags``` with ```bindings``` that can link to values from the associated Java class.


### Example

#### HTML-file

```html
<body>
	Hello <wo:str value="$someString" />
</body>
```


#### Associated java class

```java
public class MyComponent extends NGComponent {

	public String someString = "world";

	public MyComponent( NGContext context ) {
		super( context );
	}
}
```

## Dynamic tags

A dynamic tag always starts with ```<wo:``` followed by a ```tag identifier``` and then an optional list of ```bindings```.\
Dynamic tags must always be "closed", i.e. if they have no associated closing tag, you must end the "opening" tag with ```/>```

 ```<wo:tagIdentifier binding1="$someVariable" binding2="SomeConstant" />```.

* **tagIdentifier**\
identifies which dynamic tag to use. This can be a fully qualified class name ```(ng.appserver.elements.NGString)```, the simple class name ```(NGString)``` or a shortcut provided for the tag ```(str)```

* **$someVariable**\
Bindings whose value starts with a ```$``` are dynamic and resolved against the template's java class. The identifier is usually a field name or a method name on the java class, but for a full description of the mechanics of the resolution see [KeyValueCoding](key-value-coding).

* **SomeConstant**\
Bindings whose value does not start with a ```$``` are constants. Constant values can be a ```String```, ```Integer``` or a ```Double```.\
There is an exception from this rule though; if you want to pass a ```boolean``` constant, you use the values ```$true``` and  ```$false```.

#### Acknowledgements and thanks

The template parser in ng-objects is ripped off from the Woognl template parser in [Project Wonder](https://github.com/wocommunity/wonder), although without the "ognl"-part. Awesome work mostly created by Mike Schrag and maintained and improved by the WOCommunity. Lots of thanks to him and all the others!