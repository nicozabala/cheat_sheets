Una coleccion vendria a ser como un grupo, es una lista de primitives que tiene un identificador y luego puede llamarse para seleccionar todos los primitives que contenga.

### Ejemplo
```c++
def "collections" (

prepend apiSchemas = ["CollectionAPI:grass_collection", "CollectionAPI:smarties_collection"]

)

{

uniform token collection:grass_collection:expansionRule = "explicitOnly"

rel collection:grass_collection:includes = [

</grass_vars/grass_asset/geo_grass_short_mtl_grass_material>,

</grass_vars/grass_asset/geo_grass_tall_mtl_grass_material>,

]

uniform token collection:smarties_collection:expansionRule = "explicitOnly"

rel collection:smarties_collection:includes = [

</smarties_vars/Smarties/mtl_smarties_blue>,

</smarties_vars/Smarties/mtl_smarties_green>,

</smarties_vars/Smarties/mtl_smarties_orange>,

</smarties_vars/Smarties/mtl_smarties_pink>,

</smarties_vars/Smarties/mtl_smarties_purple>,

</smarties_vars/Smarties/mtl_smarties_red>,

</smarties_vars/Smarties/mtl_smarties_yellow>,

]

}