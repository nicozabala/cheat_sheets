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

print(Sdf.Path("/set/cityA/bicycle").HasPrefix(Sdf.Path("/set")))      # Returns: True
print(Sdf.Path("/set/cityA/bicycle").HasPrefix(Sdf.Path("/set/city"))) # Returns: False
print(Sdf.Path("/set/bicycle").GetCommonPrefix(Sdf.Path("/set")))      # Returns: Sdf.Path("/set")

# Shortcut for Sdf.Path("/")
root_path = Sdf.Path.absoluteRootPath
root_path == Sdf.Path("/") # Returns: True

# We'll cover in a later section how to rename/remove things in Usd,
# so don't worry about the details how this works yet. Just remember that
# an emptyPath exists and that its usage is to remove something.

src_path = Sdf.Path("/set/bicycle")
dst_path = Sdf.Path.emptyPath
edit = Sdf.BatchNamespaceEdit()
edit.Add(src_path, dst_path)


### PROPERTIES
path = Sdf.Path("/set/bicycle.size")
property_name = path.name # Be aware, this will return 'size' (last element)

# Append property to prim path
Sdf.Path("/set/bicycle").AppendProperty("size") # Returns: Sdf.Path("/set/bicycle.size")

# Properties can also be namespaced with ":" (Sdf.Path.namespaceDelimiter)
path = Sdf.Path("/set/bicycle.tire:size") 
property_name = path.name                 # Returns: 'tire:size'
property_name = path.ReplaceName("color") # Returns: Sdf.Path("/set/bicycle.color")

# Check if path is a property path (and not a prim path)
path.IsPropertyPath() # Returns: True

# Check if path is a property path (and not a prim path)
Sdf.Path("/set/bicycle.tire:size").IsPrimPropertyPath()  # Returns: True
Sdf.Path("/set/bicycle").IsPrimPropertyPath()            # Returns: False

# Convenience methods
path = Sdf.Path("/set/bicycle").AppendProperty(Sdf.Path.JoinIdentifier(["tire", "size"]))
namespaced_elements = Sdf.Path.TokenizeIdentifier("tire:size")   # Returns: ["tire", "size"]
last_element = Sdf.Path.StripNamespace("/set/bicycle.tire:size") # Returns: 'size'

# With GetPrimPath we can strip away all property encodings
path = Sdf.Path("/set/bicycle.tire:size")
prim_path = path.GetPrimPath() # Returns: Sdf.Path('/set/bicycle')
