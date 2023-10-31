Es un tipo especial de referencia en [[USD]] que puede ser "unloaded" de la escena para optimizar
Sirven para liberar geometría en viewport para trabajar en areas especificas.

Tiene dos estados: loaded y unloaded

Tienen un [[Opinions]] mas débil que [[Sublayer]] o [[Reference]].

### Que es un unloaded Payload?
El stage no va a cargar ningún asset que este "payloaded". 

Esto sirve para tenerlo visible en la estructura pero no cargarlo, ademas vienen con algunos datos por ejemplo [[AssetInfo]], [[Variant]] o BoundingBox.
