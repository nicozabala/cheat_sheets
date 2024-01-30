El principal funcion de los prim es la de definir y almacenar propiedades. La clase prim en si contiene muy poca data:

- Path/Name
- Coneccion a sus propiedades
- Metadata realacionada a Composition y Schemas, como tambien "core" metadata (specifier, kind, typeName, activation, assetInfo, customData)

## Prim Basics
### High Level
Para setear metadata en High Level, no se hace directo sobre el prim sino sobre schemas, por ejemplo para settear un Kind, se hace mediante el schema Usd.ModelAPI

```python
from pxr import Kind, Sdf, Usd
stage = Usd.Stage.CreateInMemory()
prim_path = Sdf.Path("/cube")
prim = stage.DefinePrim(prim_path, "Xform") # Here defining the prim uses a `Sdf.SpecifierDef` define op by default.
# The specifier and type name is something you'll usually always set.
prim.SetSpecifier(Sdf.SpecifierOver)
prim.SetTypeName("Cube")
# The other core specs are set via schema APIs, for example:
model_API = Usd.ModelAPI(prim)
if not model_API.GetKind():
    model_API.SetKind(Kind.Tokens.group)

```

### Low Level
En Low Level hay varias formas de setear la core metadata mediante atributos de clase standard.

```python
### MODO 1
from pxr import Sdf
layer = Sdf.Layer.CreateAnonymous()
prim_path = Sdf.Path("/cube")
prim_spec = Sdf.CreatePrimInLayer(layer, prim_path) # Here defining the prim uses a `Sdf.SpecifierOver` define op by default.
# The specifier and type name is something you'll usually always set.
prim_spec.specifier = Sdf.SpecifierDef # Or Sdf.SpecifierOver/Sdf.SpecifierClass
prim_spec.typeName = "Cube"
prim_spec.active = True # There is also a prim_spec.ClearActive() shortcut for removing active metadata
prim_spec.kind = "group"    # There is also a prim_spec.ClearKind() shortcut for removing kind metadata
prim_spec.instanceable = False # There is also a prim_spec.ClearInstanceable() shortcut for removing instanceable metadata.
prim_spec.hidden = False # A hint for UI apps to hide the spec for viewers
```

```python 
### MODO 2
from pxr import Sdf
layer = Sdf.Layer.CreateAnonymous()
prim_path = Sdf.Path("/cube")
prim_spec = Sdf.CreatePrimInLayer(layer, prim_path)
# The specifier and type name is something you'll usually always set.
prim_spec.SetInfo(prim_spec.SpecifierKey, Sdf.SpecifierDef) # Or Sdf.SpecifierOver/Sdf.SpecifierClass
prim_spec.SetInfo(prim_spec.TypeNameKey, "Cube")
# These are some other common specs:
prim_spec.SetInfo(prim_spec.ActiveKey, True)
prim_spec.SetInfo(prim_spec.KindKey, "group")
prim_spec.SetInfo("instanceable", False) 
prim_spec.SetInfo(prim_spec.HiddenKey, False)
```

## Specifiers

La funcion de los Specifiers es principalmente definir si un prim debe ser visible a "hierarchy traversals".

Los tres tipos de specifiers

```c++
def Cube "definedCube" ()
{
    double size = 2
}

over Cube "overCube" ()
{
    double size = 2
}

class Cube "classCube" ()
{
    double size = 2
}
```

Asi es como se ve afectado el "traversal"

```python
### High Level ###
from pxr import Sdf, Usd
stage = Usd.Stage.CreateInMemory()
stage.DefinePrim("/definedCube", "Cube").SetSpecifier(Sdf.SpecifierDef)
stage.DefinePrim("/overCube", "Cube").SetSpecifier(Sdf.SpecifierOver)
stage.DefinePrim("/classCube", "Cube").SetSpecifier(Sdf.SpecifierClass)
## Traverse with default filter (USD calls filter 'predicate')
# UsdPrimIsActive & UsdPrimIsDefined & UsdPrimIsLoaded & ~UsdPrimIsAbstract
for prim in stage.Traverse():
    print(prim)
# Returns:
# Usd.Prim(</definedCube>)
## Traverse with 'all' filter (USD calls filter 'predicate')
for prim in stage.TraverseAll():
    print(prim)
# Returns:
# Usd.Prim(</definedCube>)
# Usd.Prim(</overCube>)
# Usd.Prim(</classCube>)
## Traverse with IsAbstract (== IsClass) filter (USD calls filter 'predicate')
predicate = Usd.PrimIsAbstract
for prim in stage.Traverse(predicate):
    print(prim)
# Returns:
# Usd.Prim(</classCube>)
## Traverse with ~PrimIsDefined filter (==IsNotDefined) (USD calls filter 'predicate')
predicate = ~Usd.PrimIsDefined
for prim in stage.Traverse(predicate):
    print(prim)
# Returns:
# Usd.Prim(</overCube>)
```

### Sdf.SpecifierDef: def(define)
Este Specifier se usa para especificar que el prim SIEMPRE es visible a los traversals.

```python
### High Level ###
from pxr import Sdf, Usd
stage = Usd.Stage.CreateInMemory()
prim_path = Sdf.Path("/bicycle")
# The .DefinePrim method uses a Sdf.SpecifierDef specifier by default
prim = stage.DefinePrim(prim_path, "Xform")
prim.SetSpecifier(Sdf.SpecifierDef)

### Low Level ###
from pxr import Sdf
layer = Sdf.Layer.CreateAnonymous()
prim_path = Sdf.Path("/bicycle")
# The .CreatePrimInLayer method uses a Sdf.SpecifierOver specifier by default
prim_spec = Sdf.CreatePrimInLayer(layer, prim_path)
prim_spec.specifier = Sdf.SpecifierDef
```

### Sdf.SpecifierDef: over(override)
Los prim "over" solo se cargan si en otro layer fue especificado con el "def" specifier. Se utiliza cuando se quiere agregar data a una jerarquia existente, por ejemplo cuando se quiere agregar un layer de posicion y normales a un personaje, donde en el modelo base solo se especifica la topologia o las UVs.

Por defecto el stage traversal omite los prims que solo son "over", estos tampoco son pasados al Hydra delegate.

```python
### High Level ###
from pxr import Sdf, Usd
stage = Usd.Stage.CreateInMemory()
prim_path = Sdf.Path("/bicycle")
# The .DefinePrim method uses a Sdf.SpecifierDef specifier by default
prim = stage.DefinePrim(prim_path, "Xform")
prim.SetSpecifier(Sdf.SpecifierOver)
# or 
prim = stage.OverridePrim(prim_path)
# The prim class' IsDefined method checks if a prim (and all its parents) have the "def" specifier.
print(prim.GetSpecifier() == Sdf.SpecifierOver, not prim.IsDefined() and not prim.IsAbstract())

### Low Level ###
from pxr import Sdf
layer = Sdf.Layer.CreateAnonymous()
prim_path = Sdf.Path("/bicycle")
# The .CreatePrimInLayer method uses a Sdf.SpecifierOver specifier by default
prim_spec = Sdf.CreatePrimInLayer(layer, prim_path)
prim_spec.specifier = Sdf.SpecifierOver

```

### Sdf.SpecifierClass: class
Se utiliza para definir un "template" que luego podria ser asociada a otros prims. Por ejemplo un set de settings de geometria que despues pueden ser aplicados a distintas partes de la escena.

- Por defecto los traversals omiten los class prims
- USD se refiere a los class como abstract primss, porque nunca contribuyen directamente a la jerarquia
- Apuntamos a estos class prim mediente herencia, referencias o specialize.

```python
### High Level ###
from pxr import Sdf, Usd
stage = Usd.Stage.CreateInMemory()
prim_path = Sdf.Path("/bicycle")
# The .DefinePrim method uses a Sdf.SpecifierDef specifier by default
prim = stage.DefinePrim(prim_path, "Xform")
prim.SetSpecifier(Sdf.SpecifierClass)
# or 
prim = stage.CreateClassPrim(prim_path)
# The prim class' IsAbstract method checks if a prim (and all its parents) have the "Class" specifier.
print(prim.GetSpecifier() == Sdf.SpecifierClass, prim.IsAbstract())

### Low Level ###
from pxr import Sdf
layer = Sdf.Layer.CreateAnonymous()
prim_path = Sdf.Path("/bicycle")
# The .CreatePrimInLayer method uses a Sdf.SpecifierOver specifier by default
prim_spec = Sdf.CreatePrimInLayer(layer, prim_path)
prim_spec.specifier = Sdf.SpecifierClass
```

## Type Name
El typeName es para determinar a que schema el prim esta adherido. Los schemas son como clases de OOP. Tambien se puede tener un prim sin typeName, pero no es recomendable, para esto hay un "empty" schema llamado Scope.


```python
### High Level ###
from pxr import Sdf, Usd
stage = Usd.Stage.CreateInMemory()
prim_path = Sdf.Path("/bicycle")
prim = stage.DefinePrim(prim_path, "Xform")
prim.SetTypeName("Xform")

### Low Level ###
from pxr import Sdf
layer = Sdf.Layer.CreateAnonymous()
prim_path = Sdf.Path("/bicycle")
prim_spec = Sdf.CreatePrimInLayer(layer, prim_path)
prim_spec.typeName = "Xform"

# Default type without any fancy bells and whistles:
prim.SetTypeName("Scope")
prim_spec.typeName = "Scope"

```

## Kind
Es una metadata asociada a un prim para marcarla como un "tipo" de jerarquia. De esta manera es mas facil hacer el traversal y seleccionar "kinds" especificos sin atraversar todos los prim.

```python
### High Level ###
from pxr import Kind, Sdf, Usd
stage = Usd.Stage.CreateInMemory()
prim_path = Sdf.Path("/bicycle")
prim = stage.DefinePrim(prim_path, "Xform")
model_API = Usd.ModelAPI(prim)
model_API.SetKind(Kind.Tokens.component)
# The prim class' IsModel/IsGroup method checks if a prim (and all its parents) are (sub-) kinds of model/group.
model_API.SetKind(Kind.Tokens.model)
kind = model_API.GetKind()
print(kind, (Kind.Registry.GetBaseKind(kind) or kind) == Kind.Tokens.model, prim.IsModel())
model_API.SetKind(Kind.Tokens.group)
kind = model_API.GetKind()
print(kind, (Kind.Registry.GetBaseKind(kind) or kind) == Kind.Tokens.group, prim.IsGroup())

### Low Level ###
from pxr import Kind, Sdf
layer = Sdf.Layer.CreateAnonymous()
prim_path = Sdf.Path("/bicycle")
prim_spec = Sdf.CreatePrimInLayer(layer, prim_path)
prim_spec.SetInfo("kind", Kind.Tokens.component)
```


## Active
Esta metadata define si el prim y sus hijos van a ser cargados o no. Este parametro no puede ser animado, para eso se usa visibility (pruning)

```python
from pxr import Sdf, Usd
### High Level ###
stage = Usd.Stage.CreateInMemory()
prim_path = Sdf.Path("/bicycle")
prim = stage.DefinePrim(prim_path, "Xform")
prim.SetActive(False)

### Low Level ###
layer = Sdf.Layer.CreateAnonymous()
prim_path = Sdf.Path("/cube")
prim_spec = Sdf.CreatePrimInLayer(layer, prim_path)
prim_spec.active = False
# Or
prim_spec.SetInfo(prim_spec.ActiveKey, True)
```

## Debugging
```python
from pxr import Sdf
layer = Sdf.Layer.CreateAnonymous()
prim_path = Sdf.Path("/cube")
prim_spec = Sdf.CreatePrimInLayer(layer, prim_path)
prim_spec.specifier = Sdf.SpecifierDef
prim_spec.SetInfo(prim_spec.KindKey, "group")
attr_spec = Sdf.AttributeSpec(prim_spec, "size", Sdf.ValueTypeNames.Float)
# Running this
print(prim_spec.GetAsText())
# Returns:
"""
def "cube" (
    kind = "group"
)
{
    float size
}
"""
```

## Resumiendo...

### High Level
```python
from pxr import Usd, Sdf
# Has: 'HasProperty', 'HasAttribute', 'HasRelationship'
# Get: 'GetProperties', 'GetAuthoredProperties', 'GetPropertyNames', 'GetPropertiesInNamespace', 'GetAuthoredPropertiesInNamespace'
#      'GetAttribute', 'GetAttributes', 'GetAuthoredAttributes'
#      'GetRelationship', 'GetRelationships', 'GetAuthoredRelationships'
#      'FindAllAttributeConnectionPaths', 'FindAllRelationshipTargetPaths'
# Set: 'CreateAttribute', 'CreateRelationship'
# Clear: 'RemoveProperty', 
stage = Usd.Stage.CreateInMemory()
prim_path = Sdf.Path("/bicycle")
prim = stage.DefinePrim(prim_path, "Cube")
# As the cube schema ships with a "size" attribute, we don't have to create it first
# Usd is smart enough to check the schema for the type and creates it for us.
size_attr = prim.GetAttribute("size")
size_attr.Set(10)
## Looking up attributes
print(prim.GetAttributes())
# Returns: All the attributes that are provided by the schema
"""
[Usd.Prim(</bicycle>).GetAttribute('doubleSided'), Usd.Prim(</bicycle>).GetAttribute('extent'), Usd.
Prim(</bicycle>).GetAttribute('orientation'), Usd.Prim(</bicycle>).GetAttribute('primvars:displayCol
or'), Usd.Prim(</bicycle>).GetAttribute('primvars:displayOpacity'), Usd.Prim(</bicycle>).GetAttribut
e('purpose'), Usd.Prim(</bicycle>).GetAttribute('size'), Usd.Prim(</bicycle>).GetAttribute('visibili
ty'), Usd.Prim(</bicycle>).GetAttribute('xformOpOrder')]
"""
print(prim.GetAuthoredAttributes())
# Returns: Only the attributes we have written to in the active stage.
# [Usd.Prim(</bicycle>).GetAttribute('size')]
## Looking up relationships:
print(prim.GetRelationships())
# Returns:
# [Usd.Prim(</bicycle>).GetRelationship('proxyPrim')]
box_prim = stage.DefinePrim("/box")
prim.GetRelationship("proxyPrim").SetTargets([box_prim.GetPath()])
# If we now check our properties, you can see both the size attribute
# and proxyPrim relationship show up.
print(prim.GetAuthoredProperties())
# Returns:
# [Usd.Prim(</bicycle>).GetRelationship('proxyPrim'),
#  Usd.Prim(</bicycle>).GetAttribute('size')]
## Creating attributes:
# If we want to create non-schema attributes (or even schema attributes without using
# the schema getter/setters), we can run:
tire_size_attr = prim.CreateAttribute("tire:size", Sdf.ValueTypeNames.Float)
tire_size_attr.Set(5)
```

### Low Level

```python
from pxr import Sdf
layer = Sdf.Layer.CreateAnonymous()
prim_path = Sdf.Path("/cube")
prim_spec = Sdf.CreatePrimInLayer(layer, prim_path)
prim_spec.specifier = Sdf.SpecifierDef
attr_spec = Sdf.AttributeSpec(prim_spec, "size", Sdf.ValueTypeNames.Float)
print(prim_spec.attributes) # Returns: {'size': Sdf.Find('anon:0x7f6efe199480:LOP:/stage/python', '/cube.size')}
attr_spec.default = 10
# To remove a property you can run:
# prim_spec.RemoveProperty(attr_spec)
# Let's re-create what we did in the high level API example.
box_prim_path = Sdf.Path("/box")
box_prim_spec = Sdf.CreatePrimInLayer(layer, box_prim_path)
box_prim_spec.specifier = Sdf.SpecifierDef
rel_spec = Sdf.RelationshipSpec(prim_spec, "proxyPrim")
rel_spec.targetPathList.explicitItems = [prim_path]
# Get all authored properties (in the active layer only)
print(prim_spec.properties)
# Returns:
"""
{'size': Sdf.Find('anon:0x7ff87c9c2000', '/cube.size'),
 'proxyPrim': Sdf.Find('anon:0x7ff87c9c2000', '/cube.proxyPrim')}
"""

```
