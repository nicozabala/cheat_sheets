Los packages son una forma de configurar Houdini y adaptarlo a nuestro modo sea agregando plugins o modificando aspectos graficos.

Reemplaza todo lo que se hacia antes en houdini.env

Para utilizarlos es necesario tener un directorio "packages" en alguno de estos lugares.
```
$HOUDINI_USER_PREF_DIR/packages

$HSITE/houdinimajor.minor/packages (for example, $HSITE/houdini18.0/packages)

$HOUDINI_PACKAGE_DIR

Houdini will process the package files directly in the directory specified in HOUDINI_PACKAGE_DIR, do not add a packages directory under these folders.

$HFS/packages
```
Lo que se hace es crear un archivo .json en la carpeta /packages y se especifica el path donde se encuentra el plugin:

```json
{
    "hpath" : "/user/bob/libs"
}
```

Los keywords para este json son los siguientes:
----
**env** \
Sets or modifies environment variables.

**enable** \
Enables or disables a package.

**load_package_once** \
Prevents a package from being loaded multiple times. Houdini will load the first package in the search path with "load_package_once": true, and ignore any other packages with the same file name in the search path. This keyword defaults to false.

**process_order** \
Specifies an integer value that Houdini can use for arranging the order of the packages to process in a package directory.

**package_path** \
Scans package paths dynamically.


Houdini es extremadamente configurable, algunas de las cosas que se pueden modificar dentro de un package son por ejemplo estos archivos:

NetworkViewMenu \
OPlibraries\
OPmenu\
PaneTabTypeMenu

