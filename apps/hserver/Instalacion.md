Una vez instalada la version de Houdini solo con HServer.

```bash
# Stop license server 
systemctl stop sesinetd.service
```

```bash
# Reemplazar
cp sesinet /usr/lib/sesi/
```

```bash
# Start license server 
systemctl start sesinetd.service
```

```bash
# Copiar el Server code
sesictrl print-server
```

```
Usar el Keygen de Windows para generar los keys
```

```bash
# Instalar keys
sesictrl install ###
```