# Sessions

A session holds a user's state between requests, including the [page cache](glossary#page-cache) that [component actions](component-actions) need.

## Getting it

| | |
| --- | --- |
| `session()` | In a component. Creates the session if there's none. |
| `context.session()` | Same, elsewhere. |
| `context.existingSession()` | The session, or `null`. Never creates one. |
| `context.hasSession()` | Is there one? |

Don't create sessions you don't need: plain pages served by routes work without one.

## Your own session class

Name it `Session`, extending `NGSession`, in your application's package:

```java
public class Session extends NGSession {

	public User user;
}
```

```java
final Session session = (Session)session();
```

## Lifetime

* Expires after 60 idle minutes. *(TODO: not configurable yet.)*
* End it with `session().terminate()`.
* Kept in memory: a restart ends all sessions.

## Cookie

`ngsid`: `HttpOnly`, `SameSite=Lax`, path `/`. *(TODO: not marked `Secure` yet; override `createSessionCookie` in your application to change it.)*
