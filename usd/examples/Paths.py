from pxr import Sdf

path = Sdf.Path("/set/bicycle")
path_name = path.name ## Devuelve el ultimo elemento del path
path_empty = path.isEmpty ## Chequea si esta vacio el path
Sdf.Path.IsValidPathString("/some/_wrong!/path") ## Valida si el path esta bien generado (por el usuario)

# Join Paths
path = Sdf.Path("/set/bicycle")
newpath = path.AppendPath(Sdf.Path("frame/screws"))
print(newpath)

# Manually join individual path elements
path = Sdf.Path(Sdf.Path.childDelimiter.join(["set", "bycicle"]))
print(path)

# Get parent path
parent_path = path.GetParentPath()
print(parent_path)
print(parent_path.IsRootPrimPath())

# Devuelve un interator de los parents
ancestor_range = path.GetAncestorsRange()
print(ancestor_range)

# Agrega un child
child_path = path.AppendChild("wheel")
print(child_path)

# Chequea si es un Prim path, osea no es un attribute/relationship
print(path.IsPrimPath()) 