# Setting up for development

## You need

* **JDK ${java.release}+**
* **Maven 3.8.8+**
* **An IDE.** Any Java IDE works: import the project as a Maven project.

## Running

Run your `Application` class's `main()` from the IDE. The app runs on [localhost:1200](http://localhost:1200/), in [development mode](development-tools#development-mode).

Change the port with a program argument: `-WOPort 1300`.

## Project layout

```
pom.xml
build.properties               principalClass=…
src/main/java/                 Application, components, …
src/main/resources/
	components/                templates
	webserver-resources/       CSS, JS, images, served at /nr/app/…
	app-resources/             files for your code, and Properties
	public/                    served at the site root
```

## Faster turnaround

* Template and resource edits show on reload.
* Java edits need a restart, unless your IDE hot-swaps them. *(TODO: setting up full hot swap.)*

## Eclipse

The Parslips plugin adds template editing and validation, and lets tools drive a running app. *(TODO: installation.)*
