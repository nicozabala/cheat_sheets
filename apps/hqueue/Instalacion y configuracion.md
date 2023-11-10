Instalacion en una VM con lo siguiente:
```
Memory = 8gb
CPU = 1CPU
HDD = 32gb (Para los jobs y copiar el installer)
```

Crear en /mnt las siguientes carpetas

```bash
mkdir /mnt/hq

# Por cada share
mkdir /mnt/active
mkdir /mnt/library
mkdir /mnt/recent
mkdir /mnt/rd
```

Luego en fstab agrego los mounts

```
sudo apt update
sudo apt install cifs-tools
sudo apt instlal nano
```

```
# HQUEUE Mount Point
//10.10.10.100/HQUEUE /mnt/hq cifs guest,uid=bleed 0 0

# BLEEDFS01
//10.10.10.100/ACTIVE /mnt/active cifs guest,uid=bleed 0 0
//10.10.10.100/RECENT /mnt/recent cifs guest,uid=bleed 0 0
//10.10.10.100/LIBRARY /mnt/library cifs guest,uid=bleed 0 0
//10.10.10.100/RD /mnt/rd cifs guest,uid=bleed 0 0
```

Instalo desde /< houdini-installer >/scripts./.hqueue.install HQueue