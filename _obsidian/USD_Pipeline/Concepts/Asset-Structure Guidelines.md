Los siguientes conceptos deberían ser comunes en todos los tipos de Asset en cualquier pipeline USD:

- [[Model]] son assets en USD. Los [[Model]] publicados son de [[Kind]] [[component]] o [[assembly]], o kinds basados en ellos.
- [[component]] models assets publicables que guardan su geometry detrás de un [[Payload]]; son generalmente "self-contained" (mas allá de la referencia de los materiales)
- [[assembly]] son assets publicables que hace referencia [[component]] u otro [[assembly]]. Los [[assembly]] que generan su propio [[component]] deberían tener un [[Payload]] y asegurar una jerarquía correcta. El [[Kind]] "Group" es normalmente usado para organizar assemblies y mantener la jerarquía del [[Model]].
# Todo es un ASSET
geometria, shaders, texturas, archivos zip, caches de animacion, sonidos, notas, etc.

La estructura de assets en USD consiste en dos consideraciones:
### Primitive Hierarchy
- Los ancestros de prims con [[Kind]] component-based deben tener un grupo o [[assembly]] para ser models correctos
- Las relaciones del tipo material:binding deben apuntar a prims que estan por debajo del prim.
- Utilizar [[Scope]] para organizar prims (reduce el riesgo de transformaciones indeseadas)
- Evitar [[XForms]] 
- Optar por nombres cortos en lo posible
- Asignar [[Scope]] y [[Purpose]] a un prim lo hace mas claro y ayuda a [[Hydra]] a digerir la geo cuando se trabaja con [[USD]] en vivo.

### Composition & File Organization
- Los [[Layers]] son normalmente divididos en department/work/contribution/content
- Guardar los [[Layers]] como directorios hijo ayuda a la portabilidad y a los paths relativos
- Los [[Layer]] de elemento individual son generalmente referenciados o [[Sublayer]] 
- Usar [[Reference]] ayuda a mantener consistente las [[Opinions]], cada contribucion es la "R" en [[LIVRPS]]
- El minimo para un asset razonable [[USD]] es asset.usd y payload.usd
- Utilizar la extension .usd es lo mas recomendable para el asset.usd, para evitar tener que modificar las referencias si el asset layer cambia de binario a ascii.
- Organizar cada asset en sub-carpetas. Ej. /model, /lgt, /vfx
- Dentro de las capas de los layers tambien es recomendado hacer subcarpetas por ejemplo: /maps, /vol, /cache

### Versioning the structure
- El estructurado de assets debería ser flexible
- Mediante metadata o en archivos, se pueden escribir sistemas para entender que tan flexible es editar o contribuir a un asset.
- Al referenciar un asset, no debería importar esto, es mas para los artistas que están trabajando o los programas que acceden a los assets para editarlos.
- La unica parte del pipeline USD específicamente diseñada para ayudar en el Version Control son los [[Asset Resolver]] plugins.

## Component


