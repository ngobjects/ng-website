# KeyValueCoding

KeyValueCoding is the mechanism by which templates link the values of ```dynamic bindings``` to their associated java class.\
When you write out a dynamic binding in a template, say something like ```<wo:str value="$someName" />```, the template will attempt to resolve ```someName``` against the java class in the following order, returning the value from the first implemented method:

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
13. Finally, if none of these methods work out, an ```NGKeyValueCoding.UnknownKeyException``` will be thrown.



## KeyPaths

The paths in dynamic bindings can have multiple components, separated by a period, and we call them ```KeyPaths```.

If you write ```<wo:str value="$company.manager.name" />``` the object graph will be traversed through that path and the lookups specified above are performed on the value returned by each component of the path to end up with the final value.


### ```Nulls``` in keyPaths

If any component of the keyPath returns ```null```, say, if you write ```company.manager.name``` and ```manager``` returns null, the entire keyPath will resolve to null instead of throwing a ```NullPointerException``` like you might expect in Java.\
It's much like working in a language with a null safe navigation operator and spell out the path as "company?.manager?.name", but the operator is implied.