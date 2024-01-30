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
