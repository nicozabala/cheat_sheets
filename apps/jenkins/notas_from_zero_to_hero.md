Jenkins es un Automation Platform que permite:
- Build
- Test
- Deploy

No solo sirve para el desarrollo de software sino para automatizar cualquier tarea

Jenkins Infrastructure:

### Master Server
- Controla Pipelines
- Schedule Builds

### Agent/Nodes
- Perform the build

Hay dos tipos, los Cloud Agents y los Permanent Agents.

Los Permanent Agents son servers (linux o win) que seran los que se encargaran de ejecutar las tareas, sea compilar por ejemplo. 

Los Cloud Agent pueden ser Docker, AWS o Kubernetes

Jenkins trabaja con dos tipos de procesos:
#### Freestyle Build
Es el mas simple y se maneja muy parecido a shell scripts

#### Pipelines
Usando la sintaxis Groovy, se programan "steps" para automatizar

