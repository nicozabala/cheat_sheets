Primero generar un SSH Keypair:

```sh
ssh-keygen -t rsa
```
Copiar el Private Key en:

Manage Jenkins > Credentials > Add Key

SSH User and Pass

Ponerle un ID y pegar la PrivateKey

Ahora ir al proyecto que se desea acceder en Github, ir a Settings > Deploy Keys y pegar la Public Key.

Siguiente paso es muy **importante!** Conectarse a la consola de jenkins (ssh, portainer, exec, etc) e intentar conectarse al repositorio para generar los fingerprints! ***Atento que esto hay que hacerlo en todos los agents***

```bash
git ls-remote -h git@github.com:nicozabala/dcore.git
```

Darle "Yes"! 

Ahora un pipeline script de Jenkins deberia verse asi:

```groovy
pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                script {
                    // Clean workspace before cloning
                    deleteDir()

                    // Clone the Git repository using SSH key credentials
                    git branch: 'main',
                        credentialsId: 'id_rsa',
                        url: 'ssh://git@github.com/nicozabala/dcore.git'
                }
            }
        }
    }

    post {
        success {
            echo 'The pipeline has successfully completed.'
        }
        failure {
            echo 'The pipeline has failed.'
        }
    }
}
```

Tambien se puede usar un Freestyle Project, pero recordar en el url usar este formato (porque es SSH):
```
git@github.com:nicozabala/dcore.git
```

Ahi deberia hacer el checkout bien!