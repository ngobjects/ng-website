# Getting started

Let's go through a quick creation of an application and a couple of routes. This shouldn't take more than 5 minutes to complete.

#### Creating the project

Start by creating a standard maven project. Make sure you're using Java 17 or newer and add the following dependency:

```xml
<dependency>
    <groupId>${maven.groupId}</groupId>
    <artifactId>${maven.artifactId}</artifactId>
    <version>${maven.version}</version>
</dependency>
```


Now create a class called Application.java and paste in the following code:

```java
package ng.website;

import ng.appserver.NGApplication;

public class Application extends NGApplication {

	public static void main( String[] args ) {
		NGApplication.run( args, Application.class );
	}
}
```

Run this class as a java application and point your browser to [http://localhost:1200/](http://localhost:1200/).

Congratulations, your first application is up and running!

#### Creating a route

Now, let's add our first route. In the Application class you created earlier

#### Creating and viewing a component

(demonstrate a route re

#### Embedding your own component

#### Creating a wrapper component