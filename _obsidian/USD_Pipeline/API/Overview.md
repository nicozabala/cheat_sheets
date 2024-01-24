El API esta dividido en dos niveles

**pxr**
	|---High Level (Usd)
    |---Low Level ([[PcP]]/[[Sdf]])

Ambas formas de usar el API son validas, siendo la High Level mas amigable para aprender y ademas implementa los Get() Set(), pero a su vez es mas optimo usar el Low Level lo mas que se pueda por su velocidad.

Otros módulos base que suplementan a estos dos API levels son:
**Gf**: Graphics Foundation, acá están las clases relacionadas con math y utility (matrix and vector classes, por ejemplo)
**Vt**: Value Type, provee de que tipos de datos USD puede almacenar, entre estos se encuentra Vt.Array que permite mapear USD Arrays a numpy arrays.
**Plug**: Este modulo maneja el framework de Plugins de USD
**Tf**: Tools Foundation, profiling, debugging y utilidades C++.

```python
### High Level ###

from pxr import Sdf, Usd
stage = Usd.Stage.CreateInMemory()
prim_path = Sdf.Path("/bycicle")
prim = stage.DefinePrim(prim_path, "Xform")
attr = prim.CreateAttribute("tire:size", Sdf.ValueTypeNames.Float)
attr.Set(10)
```

```python
### Low Level
from pxr import Sdf
layer = Sdf.Layer.CreateAnonymous()
prim_path = Sdf.Path('/bycicle')
prim_spec = Sdf.CreatePrimInLayer(layer, prim_path)
prim_spec.specifier = Sdf.SpecifierDef
prim_spec.typeName = "Xform"
attr_spec = Sdf.AttributeSpec(prim_spec, "tire:size", Sdf.ValueTypeNames.Float)
attr_spec.default = 10
```

### Cuando usar cual?
***High Level*** = Leer data del Stage, usar Usd Schema Classes (UsdGeomMesh, UsdClipsAPI, UsdGeomPrimvarsAPI)

***Low Level*** = Crear, copiar, modificar data de un layer, se requiere performance

### High Level API
Basicamente todo lo que esta en pxr.Usd wrapea cosas de pxr.Sdf o pxr.Pcp poniendole getter/setters, clases de conveniencia y funciones.

Es mas OOP y usa design patterns de C++.

Este nivel siempre opera sobre el Stage, esto significa que siempre que haya Stages, se esta usando el High Level. Tambien se encarga de hacer validaciones de data/settings.

### Low Level API
Este nivel siempre opera layers individuales, no tendremos accesos al Stage (aka, layers compuestas)


