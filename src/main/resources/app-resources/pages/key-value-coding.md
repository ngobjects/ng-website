| 💡 **Fun fact**\
KeyValueCoding comes from Apple's `NSKeyValueCoding`. `NGKeyValueCoding` behaves the same, so if you know that, you know this.

# KeyValueCoding

KVC resolves a binding like `$name` to a method or field on the component.

## Reading

First match wins. Public members only.

1. `getName()`
2. `name()`
3. `isName()`
4. `_getName()`
5. `_name()`
6. `_isName()`
7. field `name`
8. field `_name`
9. field `_isName`
10. field `isName`

No match throws `UnknownKeyException`, with a suggestion: *"Did you mean 'name'?"*. In a template, it shows as an error box in the page.

## Setting

Forms set bindings on submit.

1. `setName( value )`
2. field `name`

Strings are converted when the target is a number.

## Keypaths

`$company.manager.name` resolves each key on the result of the previous one.

A `null` anywhere makes the whole keypath `null`, with no `NullPointerException`. Setting through a `null` fails.

## Maps and custom lookups

Maps aren't supported: `$map.key` doesn't read the map's entry ([#36](https://github.com/ngobjects/ng-objects/issues/36)). To customise lookups, implement `NGKeyValueCoding` (`valueForKey`, `takeValueForKey`).

## From Java

```java
Object name = NGKeyValueCoding.Utility.valueForKey( user, "name" );
NGKeyValueCoding.Utility.takeValueForKey( user, "Jane", "name" );
```

Lookups are cached per class and key in production, but not in development.
