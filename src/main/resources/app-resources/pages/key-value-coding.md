# KeyValueCoding

KeyValueCoding is the mechanism by which templates link values of ```dynamic bindings``` to their associated java class.\
In most cases, what you will be linking to is a field or a method with the same name as the binding. But behind the scenes, more is going on. When you write out a dynamic binding in a template, say something like ```<wo:str value="$someName" />```, the template will attempt to dynamically resolve ```someName``` against the java class in the following order, returning the value from the first implemented method:

1. If class implements ```NGKeyValueCodingAdditions``` invoke ```public Object valueForKeyPath( String )``` with "someName" as a parameter
2. If class implements ```NGKeyValueCoding``` invoke ```public Object valueForKey( String )``` with "someName" as a parameter
3. Check for method ```getSomeName()```
4. Check for method  ```someName()```
5. Check for method  ```isSomeName()```
6. Check for method  ```_getSomeName()```
7. Check for method  ```_someName()```
8. Check for method  ```_isSomeName()```
9. Check for field ```_someName```
10. Check for field ```_isSomeName```
11. Check for field ```someName```
12. Check for field ```isSomeName```
13. Finally, if none of these methods work out, an ```NGKeyValueCoding.UnknownKeyException``` is thrown.

This lookup is done by ```NSKeyValueCodingAdditions.Utility::valueForKeyPath( Object object, String key )``` which is public API and you can use to perform a similar lookup.

| 💡 **Fun fact**\
As is probably obvious for those in the know, the KeyValueCoding concept originates With Apple's Foundation library's ```NSKeyValueCoding``` which is heavily used by WebObjects.\
\
 Our implementation, ```NGKeyValueCoding``` basically duplicates the behaviour of Apple's implementation, so if you're familiar with that you're good to go. 

## KeyPaths

Dynamic bindings can have multiple components, like method chaining in Java. And like in Java, components are separated by a period. When a binding has multiple components, we refer to them as ```KeyPaths``` (while single component paths are usually referred to as ```keys```).

If you write ```<wo:str value="$company.manager.name" />``` the object graph will be traversed through that path and the lookups specified above will be performed on the value returned by each component of the path to get the final value.


### ```Nulls``` in keyPaths

If any component of the keyPath returns ```null```, say, if you write ```company.manager.name``` and ```manager``` returns null, the entire keyPath will resolve to null instead of throwing a ```NullPointerException``` like you might expect in Java.\
It's much like working in a language with a null safe navigation operator and spell out the path as "company?.manager?.name", but the operator is implied.