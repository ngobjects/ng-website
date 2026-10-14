# Configuration

## Sources

Highest priority first:

1. Program arguments: `-Key value`, or `-Dkey=value` (also sets a Java system property).
2. `src/main/resources/app-resources/Properties`, a standard Java properties file:

```properties
shop.currency=EUR
```

## Reading

```java
final String currency = application().properties().get( "shop.currency" );
final Integer pageSize = application().properties().getInteger( "shop.pageSize" );
```

`null` when unset. *(TODO: typed properties and defaults.)*

## Framework properties

| Property | |
| --- | --- |
| `WOPort` | HTTP port. Default `1200` |
| `WOHost` | Host name |
| `WOApplicationName` | App name, as wotaskd knows it |
| `WOMonitorEnabled` | `YES` in deployment: turns development mode off |
| `WOLifebeatEnabled`, `WOLifebeatDestinationPort`, `WOLifebeatInterval` | Lifebeats to wotaskd |
| `WOOutputPath` | Send console output to a file |
