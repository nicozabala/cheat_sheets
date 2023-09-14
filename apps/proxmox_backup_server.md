### Recomendaciones sobre configuracion de Proxmox Backup Server

- Instalarlo on-premise en lo posible, para no tener que configurar network paths, permisos y routes.
- La version free cumple todas las necesidades, solo por el soporte es distinta

## Configurar en el boot network paths

```bash
# En el archivo /etc/fstab se agregan los paths NFS de los shares

IP:SHAREPATH MOUNTPOINT nfs defaults 0 0

# Ejemplo
10.10.42.106:/mnt/BLEEDPOOL03/ACTIVE /mnt/bleedfs01/active nfs defaults 0 0
```

## Realizar backups automaticamente
Para esto se usa <html><b>cron</b></html> que es una herramienta que esta en la mayoria de los distros de linux, es un servicio que hace de scheduler de tareas. En Proxmox Backup Server ya viene instalado por defecto.

Es una buena practica crear archivos de scripts para que <html><b>cron</b></html> ejecute estos y no los comandos en si. 

El proceso seria:

```bash
# Crear archivo de script
touch /home/scripts/run_backups.sh

# Agregar permiso de ejecucion
chmod u+x /home/scripts/run_backups.sh

# Editar el archivo
nano /home/scripts/run_backups.sh
```
```bash
#!/bin/sh

echo "Iniciando Backups"
# Se guarda el password al PBS en una variable de entorno
export PBS_PASSWORD='miPassword' 

# Se ejecuta el proceso de backup
# En este caso como el Datastore esta local solo poniendo su nombre en repository alcanza, pero aca se pueden especificar usuarios, etc.

proxmox-backup-client backup nombre.pxar:/directorio_a_backupear -ns nombre --repository NOMBRE_DATASTORE

# Se sobre-escribe la variable para que no quede rastro de la password
export PBS_PASSWORD='' 
```

Ahora solo queda configurar el cron con su schedule:
```bash
crontab -e
```
Este comando abre el editor predeterminado en el config de cron. Aca es donde en cada renglon se define un task con su respectiva frecuencia.

```bash
# El tiempo se determina [min] [hour] [dayofmonth] [month] [day of week] [command], los asteriscos (*) significan any. 

# En el siguiente ejemplo, se ejecuta el script todos los dias a la 1AM

0 1 * * * /home/scripts/./run_backups.sh
```
Cuando se cierra el editor, se guarda y ya esta listo el cron para actuar cuando haya sido configurado

## Importante
<html><b>cron</b></html> utiliza el Local Time, al igual que PBS, que se puede ver con:

```bash
timedatectl
```
