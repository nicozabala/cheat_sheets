### Chequear estado de cron
```bash
systemctl status cron
```
#### Si llega a estar inactivo
```bash
service cron start
```

#### Para que se inicia siempre que bootea el os
```bash
service cron enable
```