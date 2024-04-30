En portainer

-Descargar la ultima imagen: jenkins/jenkins:latest
-Crear volumen para jenkins
-Crear container y exponer puertos 8080:8080 y 50000:50000


```sh
sudo docker run -d --network host -v jenkins_home:/var/jenkins_home --name jenkins_server jenkins/jenkins:latest
```

-Conectarse
-Hacer el initial setup

# Setup jenkins node SSH

El Node u Agent no es mas que otra pc con java que procesa los pipelines. La manera mas eficiente que encontre de configurarlo y usarlos es via SSH.
Para esto en cualquier vm linux es necesario instalar (yo use Ubuntu Server):

**Java**

```sh
sudo apt update
sudo apt install default-jdk
```

**Docker**
```sh
sudo apt install docker.io
```

Luego crear un usuario (si es que ya no existe) de jenkins y darle permisos para correr docker y de sudo:

## Usuario jenkins

```sh
sudo adduser jenkins
sudo groupadd docker ##Esto agrega un grupo docker si es que ya no existe
sudo usermod -aG docker jenkins

### Para que se aplique correctamente la politica es necesario re-logearse con jenkins
```

## Crear carpeta para el agent
Es necesario crear una carpeta para que jenkins guarde sus archivos y lo mas importante, los Workspace.

```
sudo mkdir /home/jenkins/jenkins-agent
```

## Credenciales
Ahora desde el server de Jenkins es necesario pasarle la public key, esto se puede hacer via scp:

```sh
scp -v /home/nico/.ssh/id_rsa.pub jenkins@192.168.1.45:/home/jenkins
```

Ahora desde la consola desde el agent necesitamos agregar la public key a las autorizadas:

```sh
sudo cat /home/jenkins/id_rsa.pub >> /home/jenkins/.ssh/authorized_keys
sudo chmod 600 ~/.ssh/authorized_keys
sudo chmod 700 ~/.ssh
sudo service ssh restart
```

Resta generar los fingerprints desde el Server Jenkins al Nodo, para esto solo con conectarse via ssh alcanza:

```sh
ssh jenkins@192.168.1.45 
```

## Fingerprints Github
Para que github nos permita acceder a un repositorio privado necesitamos generar fingerprints, para esto es necesario conectarse una vez por consola

```sh
git ls-remote -h git@github.com:nicozabala/dcore.git
```

