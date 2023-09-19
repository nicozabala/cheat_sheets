### Instalacion de nodo para render vray / deadline

El nodo va a correr el OS Rocky Linux, es lo que era CentOS y sigue a la par las mejoras de RHEL.

La instalacion de Rocky Linux es bastante simple:
- Descargar .iso de la web oficial (version boot)
- Crear usb booteable en Balena Etcher
- Bootear la PC con el usb y seguir los pasos
- En este caso se instala la version Server sin GUI, y se seleccionaron algunos features (importante SSH)
- No se crea usuario, solo el root
- El hostname se modifica despues

Una vez instalado el os, todo el proceso de instalacion se hace en *root*

Suponiendo que este nodo esta conectado a un Network accesible, voy copiando via ssh los instaladores.

#### Instalacion V-Ray Standalone 
La version que se utilizo es:
```bash
vraystd_adv_61009_centos7_clang-gcc-6.3
```
La instalacion casi todo va por defecto, salvo la asignacion del servidor de licencia, en este caso se usa "Remote" y se pone la ip del server de licencias y su Puerto:
```
ej. 10.10.20.208:30304 # Ese es el puerte default de vrl
```

En caso de que se asigne mal el VRL, se puede usar el comando
```bash
/usr/ChaosGroup/V-Ray/Standalone/bin/setvrlservice
```

#### Instalacion Deadline Client
Antes que nada hay que montar el DeadlineRepository via nfs

Por si 


### SELinux
Este sistema de seguridad bloquea sesinetd
```bash
# Muestra el estado de SELinux
sestatus

# Desactiva temporalmente SELinux
setenforce 0
```

