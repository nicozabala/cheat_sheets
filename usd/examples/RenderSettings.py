from pxr import UsdGeom, Sdf, UsdRender
from pxr.Gf import Vec2i

node = hou.pwd()
stage = node.editableStage()


# Creo el Prim RenderSettings, este usa RenderSettings y RenderSettingsBase
settings = UsdRender.Settings.Define(stage, Sdf.Path("/Render/settings"))

# La resolucion se define con un vector 2di
res = Vec2i(1920,1080)

# Tomo la camara
cam = stage.GetPrimAtPath(Sdf.Path("/cameras/camera1"))

# Seteo la resolucion
settings.CreateResolutionAttr(res)

# Seteo un Relationship para el attr "camera", es el rel que devuelve GetCameraRel()
settings.GetCameraRel().SetTargets([cam.GetPath()])

print(settings.GetCameraRel().GetTargets())
print(settings.GetResolutionAttr().Get())

# Le aplico el api de Karma, importante el GetPrim()
settings.GetPrim().ApplyAPI("KarmaRenderSettingsAPI")