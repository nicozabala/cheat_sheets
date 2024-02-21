Para instalar el jenkins agent primero es necesario en el server donde esta Jenkins (puede ser el Portainer) generar ssh-keys

```sh
ssh-keygen -t rsa
```

Si no esta instalado el agent de ssh:

```sh
sudo apt update
sudo apt install openssh-client
```

Agregar la private key:
```sh
ssh-add id_rsa
```

Ahora, copiar la Public Key
```sh
cat id_rsa.pub
```

Lo siguiente es crear un container con el agent, par esto:

```sh
docker run -d --rm --name=agent --publish 2200:22 -e "JENKINS_AGENT_SSH_PUBKEY=<public_key>" jenkins/ssh-agent
```

En Jenkins, ir Manage Credentials, y agregar una credencial ssh sin username pero con la private key. (Este paso o el del ssh-agent puede que sea redundante, no se cual esta funcionando xD)

Al crear el Agent, seleccionar SSH, poner la IP y la credencial previamente creada.