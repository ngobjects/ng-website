# Getting started


Start by creating a standard maven project. Make sure you're using Java 17 or newer and add the following dependency:

```
<dependency>
    <groupId>the.group.we.will.pick</groupId>
    <artifactId>the.name.we.will.pick</artifactId>
    <version>0.64.0</version>
</dependency>
```

####

Now create a class called Application.java and paste in the following code:

```
package ng.website;

import ng.appserver.NGApplication;

public class Application extends NGApplication {

	public static void main( String[] args ) {
		NGApplication.run( args, Application.class );
	}
}
```

Finally, run this class as a regular application and point your browser to http://localhost:1200/ . Congratulations, you've got an application up and running!