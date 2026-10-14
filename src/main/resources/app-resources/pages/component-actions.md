# Component actions

A link or form calls a method on the component instance that rendered it:

```html
<wo:link action="$showDetails">Details</wo:link>
```

```java
public NGActionResults showDetails() {
	final DetailPage page = pageWithName( DetailPage.class );
	page.product = product;
	return page;
}
```

No URLs to design, nothing to parse, no state to save. The cost: actions need the user's [session](sessions) and the page kept in memory. For stable URLs, use [routes](routing).

## What an action returns

| Return | Shows |
| --- | --- |
| `null` | The same page again |
| A component | That page, which becomes the current page |
| Other `NGActionResults` (e.g. `NGResponses.ok( ... )`) | That response |

## Forms

```html
<wo:form>
	<wo:textfield value="$name" />
	<wo:submit action="$save" value="Save" />
</wo:form>
```

```java
public String name;

public NGActionResults save() {
	// name holds what was typed
	return null;
}
```

## How it works

The action URL (`/no/3.0.1.5`) names the page (`3`) and the clicked element (`0.1.5`). On click, the page is taken from the session's [page cache](glossary#page-cache) and run through the **request–response loop**:

1. **takeValuesFromRequest**: form fields set their bindings (only when there are form values).
2. **invokeAction**: the clicked element calls its action.
3. **appendToResponse**: the resulting page renders.

## The page cache

* Holds a session's last 100 pages, so the back button works.
* An evicted page's actions answer "page not found"; an expired session shows a timeout page. Sessions expire after 60 idle minutes.
* One request at a time per page. Different pages run concurrently, so synchronize state shared between them yourself.

*(TODO: cache size and session timeout aren't configurable yet.)*

To update part of a page, see [Partial page updates](partial-page-updates).
