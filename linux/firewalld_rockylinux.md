Rocky Linux viene con firewalld instalado

Para abrir un puerto hay que hacer lo siguiente

```bash
sudo systemctl status firewalld.service
sudo firewall-cmd --zone=public --permanent --add-port 20207/udp
sudo firewall-cmd --reload
```

Y para chequear de que este bien cargado:

```bash
sudo firewall-cmd --list-all
```