# Deployment

| 🚧 **Work in progress**\
Covers the basics. More to come.

## Build

```
mvn package
```

This builds `target/MyApp.woa`: your app, its libraries and a launch script.

## Run

```
./MyApp.woa/MyApp -WOMonitorEnabled YES -WOPort 2001
```

Always pass `-WOMonitorEnabled YES` in production. It turns [development mode](development-tools#development-mode) off, along with its endpoints.

## In a WebObjects environment

engifer apps run under wotaskd and JavaMonitor like WO apps. See [For WebObjects developers](wo-integration#deployment) for what's supported.

## TODO

* Running behind a reverse proxy (nginx, Apache)
* Secure session cookies
* Running without wotaskd (systemd, containers)
