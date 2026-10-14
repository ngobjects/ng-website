# Getting started

A running app with one page, in ten minutes.

| 🚧 **Pre-1.0**\
APIs change between 0.1.x releases. Code still uses the former name: `ng` packages, `NG` classes, `is.rebbi.ng` artifacts.

You need Java ${java.release}+ and Maven 3.8.8+. See [Setting up for development](setting-up).

## 1. pom.xml

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0">
	<modelVersion>4.0.0</modelVersion>
	<groupId>com.example</groupId>
	<artifactId>hello</artifactId>
	<version>1.0.0-SNAPSHOT</version>
	<packaging>woapplication</packaging>

	<properties>
		<maven.compiler.release>${java.release}</maven.compiler.release>
		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
	</properties>

	<dependencies>
		<dependency>
			<groupId>${ng.groupId}</groupId>
			<artifactId>ng-appserver</artifactId>
			<version>${ng.release}</version>
		</dependency>
		<dependency>
			<groupId>${ng.groupId}</groupId>
			<artifactId>ng-adaptor-jetty</artifactId>
			<version>${ng.release}</version>
		</dependency>
		<dependency>
			<groupId>org.slf4j</groupId>
			<artifactId>slf4j-simple</artifactId>
			<version>2.0.20</version>
		</dependency>
	</dependencies>

	<build>
		<finalName>${project.artifactId}</finalName>
		<plugins>
			<plugin>
				<groupId>is.rebbi</groupId>
				<artifactId>vermilingua-maven-plugin</artifactId>
				<version>${vermilingua.release}</version>
				<extensions>true</extensions>
			</plugin>
		</plugins>
	</build>
</project>
```

And `build.properties` next to it, naming your main class:

```properties
principalClass=com.example.hello.Application
```

## 2. Application class

`src/main/java/com/example/hello/Application.java`:

```java
package com.example.hello;

import ng.appserver.NGApplication;

public class Application extends NGApplication {

	public static void main( String[] args ) {
		NGApplication.run( args, Application.class );
	}
}
```

Run it and open [localhost:1200](http://localhost:1200/). You'll see the welcome page.

## 3. A component

`src/main/java/com/example/hello/components/Main.java`:

```java
package com.example.hello.components;

import ng.appserver.NGActionResults;
import ng.appserver.NGContext;
import ng.appserver.templating.NGComponent;

public class Main extends NGComponent {

	public int count;

	public Main( NGContext context ) {
		super( context );
	}

	public NGActionResults increment() {
		count++;
		return null;
	}
}
```

`src/main/resources/components/Main.html`:

```html
<!doctype html>
<html>
	<body>
		<p>Clicked <wo:str value="$count" /> times.</p>
		<wo:link action="$increment">Click me</wo:link>
	</body>
</html>
```

## 4. Route to it

In `Application`:

```java
@Override
public Routes routes() {
	return super.routes()
			.map( "/", Main.class );
}
```

(`import ng.plugins.Routes;` and `import com.example.hello.components.Main;`)

Restart and click the link. `increment()` runs on the same `Main` instance that rendered the page: that's a [component action](component-actions).

## 5. Build

```
mvn package
./target/hello.woa/hello
```

## Next

* [Templating](templating)
* [Creating a component](creating-a-component)
* [Glossary](glossary)
* [For WebObjects developers](wo-integration)
