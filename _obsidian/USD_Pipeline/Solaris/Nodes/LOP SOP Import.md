Trae geometría desde un SOP. 

Chequear siempre por propiedades en <span style="color:lightgreen">verde</span>.  Para no traer data animada innecesaria.

Si los SOP que se importan tienen el atributo 'name', en el graph de [[USD]] se dividen.

Si los SOP tienen un atributo 'path', al importar a [[USD]] se le asigna ese [[Path]]

Se pueden particionar las geo al importarlos a [[USD]] creando un atributo y asignándolo en "Partition Attributes". Por ejemplo crear el atributo "subset" en un grupo de polígonos. Esto es util para shading, porque se les puede asignar distintos materiales a los subsets.

Al traer objetos packeados, hay varios metodos de hacerlo. El mas optimo es usar "Create Point Instancer", es similar al Copy To Points