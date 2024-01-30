from pxr import Usd, UsdGeom, Sdf, Kind

stage = Usd.Stage.CreateNew('./Tester2.usda')
prim_path = Sdf.Path("/cube")

# Here defining the prim uses a `Sdf.SpecifierDef` define op by default.
prim = stage.DefinePrim(prim_path, "Xform") 

# The specifier and type name is something you'll usually always set.
#prim.SetSpecifier(Sdf.SpecifierOver)

prim.SetTypeName("Cube")
# The other core specs are set via schema APIs, for example:
model_API = Usd.ModelAPI(prim)
if not model_API.GetKind():
    model_API.SetKind(Kind.Tokens.group)
stage.GetRootLayer().Save()