### Instalacion en Linux
1- Descargar el server VRLService de la pagina de Chaos, es un archivo .bin. (*cgls_lin_6.0.1.bin*)

Hay que darle permisos de ejecucion
```bash
chmod +x cgls_lin_6.0.1.bin
```
Luego lo ejecutamos para instalar
```bash
sudo ./cgls_lin_6.0.1.bin
```
Hay varias opciones para esta instalacion, si lo ejecutamos desde la consola se ejecuta "no-gui" automaticamente pero sino se agrega 

```bash
-gui=0 =quit=0
```

2-
Una vez instalado se genera un archivo de configuracion en 
```yml
~/.Chaos/VRLService
```
Creo que no hay que modificar nada aca, pero por las dudas yo puse en 0.0.0.0 el host.

Ahora en \
**/usr/Chaos/VRLService**

```bash
sudo ./vrlctl online login USERNAME PASSWORD
```

Eso va a hacer que se autentifique en online en Chaos, y ya deberia tener acceso a la webui en: \
* http://serverip:30304

*Nota:*\
Lo pude instalar bien en una maquina virtual Ubuntu, por alguna razon no lo pude hacer andar en un contenedor, falla la instalacion, directamente no crea los archivos.