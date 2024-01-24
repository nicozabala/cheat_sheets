***Prim:*** "/set/bicycle" - el separador es **/**
***Property:***
	***Attribute:***"/set/bicycle.size" - el separador es **.**
	***Relationship:*** "/set.bikes \[/path/to/target/prim\]" - el separador es **.** y  \[ \]}
***Variants***: ("/set/bicycle{style=blue}wheel.size)

```python
from pxr import Sdf
# Prims
prim_path = Sdf.Path("/set/bicycle")
prim_path_str = Sdf.Path("/set/bicycle").pathString # Returns the Python str "/set/bicycle"
# Properties (Attribute/Relationship)
property_path = Sdf.Path("/set/bicycle.size")
property_with_namespace_path = Sdf.Path("/set/bicycle.tire:size")
# Relationship targets
prim_rel_target_path = Sdf.Path("/set.bikes[/set/bicycles]")           # Prim to prim linking (E.g. path collections)
# Variants
variant_path = prim_path.AppendVariantSelection("style", "blue") # Returns: Sdf.Path('/set/bicycle{style=blue}')
variant_path = Sdf.Path('/set/bicycle{style=blue}frame/screws')

```


```python
from pxr import Sdf  

path = Sdf.Path("/set/bicycle")
path_name = path.name ## Devuelve el ultimo elemento del path
path_empty = path.isEmpty ## Chequea si esta vacio el path
#print(Sdf.Path.IsValidPathString("/some/_wrong!/path")) ## Valida si el path esta bien generado (por el usuario)  

# Join Paths
path = Sdf.Path("/set/bicycle")
newpath = path.AppendPath(Sdf.Path("frame/screws"))
print(newpath)


# Manually join individual path elements
path = Sdf.Path(Sdf.Path.childDelimiter.join(["set", "bycicle", "part"]))
print(path)
```
