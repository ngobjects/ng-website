# Glossary

## In one paragraph

The [adaptor](#adaptor) receives a request and passes it to the [application](#application), which picks a [request handler](#request-handler) by [route](#route). For a [component action](#component-action), the [page](#page) is taken from the [session](#session)'s [page cache](#page-cache) and run through the [request–response loop](#requestresponse-loop). [Bindings](#binding) connect its [template](#template) to Java via [KeyValueCoding](#keyvaluecoding).

---

### Action

A method run when a link is clicked or a form submitted. It returns [action results](#action-results). See [component action](#component-action), [direct action](#direct-action).

### Action results

What an action returns: a component (the next page), a [response](#response), or `null` (same page). `NGActionResults`.

### Adaptor

The HTTP server: turns HTTP into [requests](#request) and [responses](#response) back. Jetty-based: `ng-adaptor-jetty`, or `ng-adaptor-jetty-servlet`.

### Application

The app's main object, one per running app. Starts the adaptor, holds [routes](#route), [properties](#properties) and [resources](#resource). You subclass `NGApplication`.

### Association

The object behind a binding's value: a constant (`NGConstantValueAssociation`) or a keypath (`NGKeyValueAssociation`). [Dynamic elements](#dynamic-element) read bindings through them. `NGAssociation`.

### Binding

An attribute on a [dynamic tag](#dynamic-tag), like `value="$name"`. Dynamic (`$…`, resolved with [KVC](#keyvaluecoding)) or constant; can be read and set. See [Templating](templating#binding-values).

### Binding synchronization

By default, a child component's bindings are copied into its same-named fields before each phase, and back after. To turn it off, override `synchronizesVariablesWithBindings()` and use `valueForBinding( "name" )`. See [Creating a component](creating-a-component).

### Component

An HTML [template](#template) plus a Java class extending `NGComponent`. Has state: each use is its own instance, kept between requests. See [Creating a component](creating-a-component).

### Component action

A stateful [action](#action): a method on the component that rendered the link, called on that same instance. URLs start with `/no/`. See [Component actions](component-actions).

### Content

What's between a component's tags, rendered where its template has `<wo:content />`. `NGComponentContent`.

### Context

The state of the request being handled: request, page, current component, [element ID](#element-id), session. `NGContext`. Transitional: it'll be split up later.

### Development mode

The default when running locally. Templates, resources and routes reload on every request, and the [development tools](#development-tools) are on. Off when started with `-WOMonitorEnabled YES`.

### Development tools

`/ng/dev/…` endpoints for logs, problems and evaluating code in the running app. See [Development tools](development-tools).

### Direct action

A stateless action: `somethingAction()` on an `NGDirectAction` subclass, called at `/na/ClassName/something`. Needs no session. Mostly superseded by [routes](#route).

### Dynamic element

A stateless building block, like `<wo:str>` (`NGString`). One instance serves every render, so state lives in [associations](#association), not fields. Subclass `NGDynamicElement`. See [Creating a dynamic element](creating-a-dynamic-element).

### Dynamic resource

Content generated for one request, like `<wo:img data="$bytes" />`. Served once from `/nd/`.

### Dynamic tag

A `<wo:…>` tag. Stands for a dynamic element or a component; its attributes are bindings.

### Element

Anything in a template's tree: a dynamic element, a component or static HTML. `NGElement`.

### Element ID

An element's position in the page, like `0.1.5`. Routes a click back to its element. `NGElementID`.

### Key

A name resolved with KVC: `name` in `$name`.

### KeyPath

Keys joined with periods: `$user.address.city`. A `null` along the way makes it `null`.

### KeyValueCoding

The rules for finding a method or field by name. KVC for short. `NGKeyValueCoding`. See [KeyValueCoding](key-value-coding).

### Lifebeat

A regular "I'm alive" signal from a deployed app to wotaskd, so JavaMonitor can manage it.

### Namespace

Keeps resources and components apart: the app's are in `app`, the framework's in `ng`, each [plugin](#plugin)'s in its own. The `app` in `/nr/app/logo.png`.

### ng, ng-objects

engifer's former name, still used in code: `NG` classes, `ng.` packages, `is.rebbi.ng` artifacts.

### Page

The top-level component, rendering the whole document. Created by `pageWithName( SomePage.class )` or a route.

### Page cache

A session's last 100 pages, so their component actions still work. One request at a time per page. `NGPageCache`.

### Partial page update

Re-rendering part of a page without reloading it, with the Ajax elements. See [Partial page updates](partial-page-updates).

### Plugin

Adds elements, routes and resources under its own namespace. `NGPlugin`. See [Plugins](plugins).

### Properties

App configuration: an `app-resources/Properties` file, overridden by arguments like `-WOPort 1300`. See [Configuration](configuration).

### Public resource

A file in `src/main/resources/public`, served at the site root: `public/robots.txt` → `/robots.txt`.

### Request

What the browser sent. Immutable once received. `NGRequest`.

### Request handler

Answers one kind of URL: component actions (`/no/`), direct actions (`/na/`), resources (`/nr/`), …. `NGRequestHandler`.

### Request–response loop

The phases a page goes through on a component action:

1. **takeValuesFromRequest**: form values go into bindings.
2. **invokeAction**: the clicked element runs its action.
3. **appendToResponse**: the next page renders.

A plain page view only runs `appendToResponse`.

### Resource

A file the app uses: `webserver-resources` (served at `/nr/app/…`), `app-resources` (for Java code) or `public` (site root). See [Resources](resources).

### Response

What's sent back. Make one with `NGResponses.ok( … )`. `NGResponse`.

### Route

Maps a URL to a page, a function or a request handler. See [Routing](routing).

### Session

A user's state between requests, including their page cache. Created on first use, kept by cookie, expires after 60 idle minutes. `NGSession`. See [Sessions](sessions).

### Tag name

The name after `wo:`: a short name like `str`, or a class name like `ProductList`.

### Template

A component's HTML, with dynamic tags: `components/Foo.html` or `components/Foo.wo/Foo.html`.

### Truthy, falsy

How a binding tested as a condition is read, as in `<wo:if condition="$items">`. Falsy: `null`, `false` and numbers equal to zero. Everything else is truthy, including empty strings, empty collections and the strings `"false"`, `"no"` and `"0"`. `0.5` and `NaN` are truthy. `NGAssociationUtils.isTruthy()`.

Coming from WebObjects: WO also treats empty strings and collections as true. But it reads the strings `"no"`, `"false"`, `"nil"`, `"null"` and `"0"` as false, and truncates numbers, so `0.5` is false. Such conditions behave differently after porting.

### WOA

A built app bundle (`MyApp.woa`) with a launch script, in WebObjects' format. Built by vermilingua.

### WOD file

WO-style element declarations, separate from the HTML. Supported for porting. See [Templating](templating#wod-files).

### Wrapper

A component that wraps content (layout, navigation) using `<wo:content />`.
