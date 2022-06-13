# Glossary

### Adaptor

The web server part, whose job it is to abstract our API from working with raw HTTP.

It accepts HTTP requests, converts them to an ```NGRequest``` object and forwards them to ```NGApplication.dispatchRequest()```.\
That returns an ```NGResponse``` which the adaptor will convert to a raw HTTP response and return to the client.

Our main adaptor is currently Jetty based (found in the project ```ng-adaptor-jetty```), but an experimental socket-based adaptor ```NGAdaptorRaw``` is also included in ```ng-appserver```.

### Binding

Dynamic tags can have multiple bindings, shown in templates as attributes on Dynamic Tags. Bindings are the mechanism by which values are passed between the template and the dynamic tag's class.

### Dynamic Element

Basically a lightweight programmatically created Component. An example of such a dynamic tag is ```<wo:str />``` which represents the Dynamic Element class ```NGString```.

### Dynamic Tag

Tags used in templates that get processed by our template engine. A Dynamic tag always represents either a Dynamic Element or a Component. Dynamic tags have an API that is consumed through the use of bindings.

### Component

A page or a reusable component that can be embedded in a page. Usually consists of an HTML template and an associated java class.

### KeyValueCoding


### KeyPath


### Template

The 