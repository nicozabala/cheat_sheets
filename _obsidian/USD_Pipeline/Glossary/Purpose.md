Es un atributo que se puede usar para darle a un prim y sus descendientes un "visibility flag" de alto nivel para el contexto de render.

Por ejemplo si un prim tiene su "purpose" asignado como "render", este sera excluido cuando se desee hacer un render que solo levante "proxy".

En algunos casos se considera que asignar un "purpose" es [[Stage Traversal]] pero solo para render.

A diferencia de [[Kind]], "purpose" no se puede extender con valores custom.

Los "purpose" soportados son:

**default** = El prim no tiene ningún "purpose" de render especial y sera incluido en todos los [[Rendering Paths]]

**guide** = Es un tipo de "purpose" que se suele usar en aplicaciones interactivas para declarar que el prim es una guía/rig/gizmo.

**proxy** = Se reserva normalmente para tener una representación liviana de otro objeto para ser usado en viewport.

**render** = La version "Final Quality" del prim que va a ir a render. Normalmente utilizado para render offline o final quality render.

- El purpose no es un toggle exclusivo, un prim puede ser varios, proxy y render.



