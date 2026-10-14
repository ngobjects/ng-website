# Partial page updates

| 🧪 **Experimental**\
Works, but the API may change.

Run a [component action](component-actions) and re-render only part of the page.

## 1. Include the script

Once per page, e.g. in your wrapper:

```html
<wo:script namespace="ng" filename="ng-js.js" />
```

## 2. Mark what updates, and what triggers it

```html
<wo:AjaxUpdateContainer id="clock">
	<wo:str value="$now" />
</wo:AjaxUpdateContainer>

<wo:AjaxUpdateLink action="$refresh" updateContainerID="clock">Refresh</wo:AjaxUpdateLink>
```

```java
public LocalTime now() {
	return LocalTime.now();
}

public NGActionResults refresh() {
	return null;
}
```

## Elements

| Element | Tag | Key bindings |
| --- | --- | --- |
| `AjaxUpdateContainer` | `auc` | `id` (required), `elementName` (default `div`) |
| `AjaxUpdateLink` | `aul` | `action`, `updateContainerID` (several: separate with `;`) |
| `AjaxSubmitButton` | `asb` | `action`, `updateContainerID`, `value`. Submits its form. |
| `AjaxObserveField` | `aof` | `observeFieldID`, `updateContainerID`, `action`, `fullSubmit`, `debounce` (ms, default 300) |

## Forms

```html
<wo:form>
	<wo:textfield value="$name" />
	<wo:AjaxSubmitButton action="$greet" updateContainerID="greeting" value="Say hello" />
</wo:form>

<wo:AjaxUpdateContainer id="greeting">Hello <wo:str value="$name" /></wo:AjaxUpdateContainer>
```

Re-renders also run through the [page cache](glossary#page-cache), which keeps the latest render of each container.
