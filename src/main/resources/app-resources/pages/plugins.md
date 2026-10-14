# Plugins

| 🚧 **TODO**\
Writing plugins, and the tag libraries coming with them ([#78](https://github.com/ngobjects/ng-objects/issues/78)), will be documented once they're merged.

A plugin adds [elements](glossary#element), [routes](routing) and [resources](resources) to an app, under its own [namespace](glossary#namespace). The framework's own development tools are a plugin, and so is the admin console `ng-control`.

Plugins on the classpath are found automatically, through `META-INF/services/ng.plugins.NGPlugin`.
