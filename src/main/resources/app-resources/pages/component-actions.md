## Component actions

Component actions are one of the most powerful aspects of the old ```WebObjects``` framework. They are inherently stateful actions that allow for an unmatched speed of development. But like all things stateful, they have cons. In essence, the user's state is stored in a session in memory, and if the application is restarted, that state gets lost, and that user gets kicked out.

For a very simple explanation of what a stateful action is.

* A user initiates a request.
* That request has a context.
* That context keeps track of an instance of a "page" (```NGComponent```).
* The context has an ID and is cached within the session under that id.

Usually when a page is rendered, it will invoke a single method.

* ```appendToResponse()```

In the case of component actions, two other methods are invoked before ```appendToResponse()```

* ```takeValuesFromRequest()```
* ```invokeAction()```

…TODO…