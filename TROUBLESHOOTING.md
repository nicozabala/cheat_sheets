### DNS_PROBE_ERROR 
#### No resuelve los DNS aunque este bien seteado el DNS server. 
 - Verificar la hora del servidor DNS
 - En Ubuntu para reiniciar el servicio:
 
 ```bash
sudo systemd-resolve --flush-caches
systemctl restart systemd-resolved.service
sudo resolvectl flush-caches
 ```