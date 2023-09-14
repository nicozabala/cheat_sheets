## Bind9

Bind9 es un server de DNS, a continuacion los pasos que me funcionaron para instalarlo en Ubuntu 22.04


#### Instalacion en Ubuntu
````bash
# Descargo los packages
apt install bind9 bind9-utils bind9-dnsutils -y

# Chequeo los servicios, son helpers
systemctl is-enabled named
systemctl status named
````

#### Configuracion
```bash
# en /etc/default/named agregar -4 en OPTIONS
OPTIONS="-4 -u bind"
```

```bash
# en /etc/bind/named.conf.options debajo de directory
// listen port and address
listen-on port 53 { localhost; 10.10.20.206; };

// for public DNS server - allow from any
allow-query { any; };

// define the forwarder for DNS queries
forwarders { 1.1.1.1; };

// enable recursion that provides recursive query
recursion yes;

// Al final comentar la linea de IPv6
// listen-on-v6 { any; };
```
 
```bash
# Chequeo la sintaxis de la configuracion
named-checkconf
```

#### Creacion de "Zones"
Las zonas son como los dominios

```bash
# en el archivo /etc/bind/named.conf.local
zone "bleed.vfx" {
    type master;
    file "/etc/bind/zones/forward.bleed.vfx";
}

zone "20.10.10.in-addr.arpa" {
    type master;
    file "/etc/bind/zones/reverse.bleed.vfx";
}
```
```bash
# Ahora creo las carpetas de las zonas y copio el contenido default para generarlas

mkdir - /etc/bind/zones/

// Copio contenido default
cp /etc/bind/db.local /etc/bind/zones/forward.bleed.vfx
cp /etc/bind/db.127 /etc/bind/zones/reverse.bleed.vfx
```
```bash
# Modifico el archivo forward

;
; BIND data file for the local loopback interface
;
$TTL    604800
@       IN      SOA     bleed.vfx. root.bleed.vfx. (
                            2         ; Serial
                        604800         ; Refresh
                        86400         ; Retry
                        2419200         ; Expire
                        604800 )       ; Negative Cache TTL

; Define the default name server to ns1.bleed.vfx
@       IN      NS      ns1.bleed.vfx.

; Resolve ns1 to server IP address
; A record for the main DNS
ns1     IN      A       10.10.20.206

; Other domains for bleed.vfx
; Create subdomain for apps
deadline     IN      A       10.10.20.201
bleedsw01    IN      A       10.10.10.200
//etc.
```

```bash
# Modifico el archivo reverse

;
; BIND reverse data file for the local loopback interface
;
$TTL    604800
@       IN      SOA     bleed.vfx. root.bleed.vfx. (
                            1         ; Serial
                        604800         ; Refresh
                        86400         ; Retry
                        2419200         ; Expire
                        604800 )       ; Negative Cache TTL

; Name Server Info for ns1.bleed.vfx
@       IN      NS      ns1.bleed.vfx.


; Reverse DNS or PTR Record for ns1.atadomain.io
; Using the last number of DNS Server IP address: 10.10.20.206
206      IN      PTR     ns1.bleed.vfx.
201      IN      PTR     deadline.bleed.vfx
// etc
```

```bash
# Chequeo de la sintaxis

# Checking the main configuration for BIND
sudo named-checkconf

# Checking forward zone forward.atadomain.io
sudo named-checkzone bleed.vfx /etc/bind/zones/forward.bleed.vfx

# Checking reverse zone reverse.bleed.vfx
sudo named-checkzone atadomain.io /etc/bind/zones/reverse.bleed.vfx
```

### Preparacion del servicio y Firewall

```bash
# Restart named service
sudo systemctl restart named

# Verify named service
sudo systemctl status named

# Configuro ufw firewall
sudo ufw app list
sudo ufw allow Bind9
sudo ufw status

# Checking the domain names
dig @10.10.20.206 deadline.bleed.vfx

# checking PTR record or reverse DNS
dig @10.10.20.206 -x 10.10.20.201
```

Detalles de este proceso en https://adamtheautomator.com/bind-dns-server
