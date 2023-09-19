## Como compartir un directorio via NFS

### Server
En caso de que NFS Server no este instalado:
```bash
sudo apt update

# Ubuntu/Debian
sudo apt install nfs-kernel-server

# CentOS/Rocky 
sudo yum install nfs-utils
```
NFS utiliza el archivo /etc/exports para especificar que directorios compartir y que sistemas pueden acceder a ellos.

```bash
sudo nano /etc/exports

# Agregar los shares en el archivo
/path/to/shared/directory   *(rw,sync,no_root_squash)

```

- ***:** Allows any client to access the shared directory.
- **rw:** Grants read-write access.
- **sync:** Synchronizes changes to disk immediately (useful for reliability but can affect performance).
- **no_root_squash:** Allows the root user on the client to have root-level access on the server.

### Configuracion Firewall
El puerto default de NFS es <b>2049/TCP</b>


### Client
Se agrega el path en fstab
```bash
sudo nano /etc/fstab
```
```bash
server_ip:/path/to/shared/directory /mnt/nfs_share nfs defaults 0 0
```
El share se monta automaticamente en el boot, pero tambien se puede forzar mediante:
```bash
sudo mount -a
P```