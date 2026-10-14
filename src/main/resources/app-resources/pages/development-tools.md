# Development tools

## Development mode

On by default. Off when the app is started with `-WOMonitorEnabled YES`, as in [deployment](deployment).

In development mode:

* Templates, resources and routes reload on every request. Java changes need a restart, or hot swap from your IDE.
* Errors show a detailed exception page with the source around the error.
* The endpoints below are on.

## Endpoints

| URL | |
| --- | --- |
| `/ng/dev/log` | Recent console output. `?contains=…`, `?tail=…` |
| `/ng/dev/problems` | Problems rendered into pages (unknown keys, binding errors) as JSON. `?clear=true` |
| `/ng/dev/eval` | Run Java in the live app: `?snippet=…`, or POST as `text/plain`. Loopback only. |
| `/ng/dev/type` | Answers `ng` |
| `/ng/dev/terminate` | Stops the app |

IDE plugins and AI assistants use these to watch and work with a running app.

## Logging

engifer logs through [SLF4J](https://www.slf4j.org/). Add any binding, e.g. `org.slf4j:slf4j-simple` as in [Getting started](getting-started).

```java
private static final Logger logger = LoggerFactory.getLogger( MyPage.class );
```

*(TODO: shared logging configuration, [#72](https://github.com/ngobjects/ng-objects/issues/72).)*
