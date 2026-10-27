# For WebObjects developers

| 🚧 **Changing fast**\
This area is moving quickly ahead of the November conference. Expect updates.

engifer is built on WO's ideas, not a clone of it.

## The same

* Components: template plus Java class, `.wo` folders and `.wod` files included. See [Templating](templating).
* Bindings and [KeyValueCoding](templating#keyvaluecoding).
* [Component actions](component-actions): the three phases, `pageWithName()`.
* Direct actions, sessions, wrappers with `<wo:content />`, and Wonder's inline `<wo:…>` tags.
* `.woa` bundles, run by wotaskd and JavaMonitor.

## Different

* **Java collections and `java.time`**, not Foundation (`NSArray`, `NSTimestamp`, …).
* **No EOF.** Move to [Cayenne](https://cayenne.apache.org/) or another ORM first.
* **Java ${java.release}+**, a standard Maven project, the classpath instead of `NSBundle`.
* **Few annotations.** APIs are plain typed Java.
* **`NGRequest` and `NGResponse` are interfaces.** Make responses with `NGResponses`.
* **Sessions come from the context**: `session()` in a component, `context.session()` elsewhere.

## Names

| WebObjects | engifer |
| --- | --- |
| `WOApplication` | `NGApplication` |
| `WOComponent` | `NGComponent` |
| `WOContext` | `NGContext` |
| `WOSession` | `NGSession` |
| `WORequest`, `WOResponse` | `NGRequest`, `NGResponse` |
| `WODynamicElement` | `NGDynamicElement` |
| `WOAssociation` | `NGAssociation` |
| `WODirectAction` | `NGDirectAction` |
| `WOResourceManager` | `NGResourceManager` |
| `WOString`, `WOConditional`, … | `NGString` (`str`), `NGConditional` (`if`), … See [Dynamic elements](dynamic-elements) |
| `NSKeyValueCoding` | `NGKeyValueCoding` |

## URLs

| | WebObjects | engifer |
| --- | --- | --- |
| Component actions | `/wo/` | `/no/` |
| Direct actions | `/wa/` | `/na/` |
| Resources | `/wr/` | `/nr/` |

WO adaptor URLs (`/cgi-bin/WebObjects/MyApp.woa/…`, `/Apps/WebObjects/MyApp.woa/…`) work: the prefix is stripped.

## Deployment

Built into a `.woa` by [vermilingua](https://github.com/undur/vermilingua-maven-plugin). Under wotaskd and JavaMonitor:

* ✅ Lifebeats (`WOLifebeatEnabled`, `WOHost`, `WOPort`, `WOApplicationName`, `WOLifebeatDestinationPort`, `WOLifebeatInterval`)
* ✅ Stop from JavaMonitor
* ✅ Requests through the WO Apache adaptor
* ❌ Refuse new sessions *(TODO, [#55](https://github.com/ngobjects/ng-objects/issues/55))*
* ❌ Statistics *(TODO, [#55](https://github.com/ngobjects/ng-objects/issues/55))*

See [Deployment](deployment).

## Porting

*(TODO: step-by-step guide.)* The path:

1. Java collections instead of Foundation; Cayenne instead of EOF.
2. Project Wonder → [wonder-slim](https://github.com/undur/wonder-slim).
3. wonder-slim → engifer. A compatibility layer for common WO APIs is being designed.

## API differences

*(TODO)*
