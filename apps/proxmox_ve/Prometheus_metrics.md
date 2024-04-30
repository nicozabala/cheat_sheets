### Step 1 - Create Proxmox VE API User
We will create a dedicated Proxmox VE user because anonymous data collection is not permitted. This user will have read-only permissions.

Log in to your Proxmox VE host, ensure you're working as root, and add a new user into Proxmox VE with the following command:

```sh
pveum user add pve-exporter@pve -password <password>
```
pve-exporter@pve — a username of a new Proxmox VE user.
-password <password> — set a password for that user. Replace <password> with the actual password.


After that, add the role PVEAuditor for the newly created user:

```sh
pveum acl modify / -user pve-exporter@pve -role PVEAuditor
```
/ — first argument is an access control path, everything in this case.
-user pve-exporter@pve — specify the user.
-role PVEAuditor — specify role for that user.

### Step 2 - Create Linux User
In order to run the exporter as daemon, create a dedicated system user:

```sh
useradd -s /bin/false pve-exporter
```

-s /bin/false — set login shell to /bin/false in order to disable interactive login.
pve-exporter — user's login name.

### Step 3 - Create Virtual Environment
The Prometheus Proxmox VE Exporter is written in Python, and we will install it within a so called venv (virtual environment). The use of such a virtual environment makes Python dependency handling much easier compared to a regular installation with pip.

Install python3-venv with the following commands:

```sh
apt update
apt install -y python3-venv
```
And create a new virtual environment:

```sh
python3 -m venv /opt/prometheus-pve-exporter
```
### Step 4 - Install Prometheus Proxmox VE Exporter

Activate the virtual environment:

```sh
source /opt/prometheus-pve-exporter/bin/activate
```

Check if (prometheus-pve-exporter) is present in front of your command line prompt before executing the next command.

Console: create and activate virtual environment

## Install prometheus-pve-exporter:

```sh
pip install prometheus-pve-exporter
```

On Debian 10, the error message Failed building wheel for MarkupSafe may be displayed. This is not an issue, simply verify that everything has been installed by executing the command again. It should finish in very short time and all lines should begin with Requirement already satisfied.

Finally, leave the virtual environment by executing deactivate.

```sh
deactivate
```

### Step 5 - Configure Prometheus Proxmox VE Exporter
Place the previously created credentials for Proxmox VE user pve-exporter@pve in the /etc/prometheus/pve.yml file.

```yml
default:
    user: pve-exporter@pve
    password: <password>
    verify_ssl: false
```

Also, set the file owner and the permissions:

```sh
chown -v root:pve-exporter /etc/prometheus/pve.yml
chmod -v 640 /etc/prometheus/pve.yml
```

### Step 6 - Create Systemd Service
Add the following content to the /etc/systemd/system/prometheus-pve-exporter.service file:

```sh
[Unit]
Description=Prometheus Proxmox VE Exporter
Documentation=https://github.com/prometheus-pve/prometheus-pve-exporter

[Service]
Restart=always
User=pve-exporter
ExecStart=/opt/prometheus-pve-exporter/bin/pve_exporter --config.file /etc/prometheus/pve.yml

[Install]
WantedBy=multi-user.target
Reload systemd, enable and start the service.
```

```sh
systemctl daemon-reload
systemctl enable prometheus-pve-exporter.service
systemctl start prometheus-pve-exporter.service
```

Verify that pve_explorer is listening to TCP port 9221 (which is the default) with the ss -lntp | grep 9221 command. The output should look similar like this:

```sh
LISTEN 0      128          0.0.0.0:9221      0.0.0.0:*    users:(("pve_exporter",pid=866529,fd=5),("pve_exporter",pid=866529,fd=3))
```

In some configurations it is necessary to note the IP address in front of :9221. You will need it in the next step. Normally pve-exporter binds to 0.0.0.0, which means that you can reach the exporter over every interface.

### Step 7 - Test functionality
Access the endpoint which provides the metrics via curl.

```sh
curl --silent http://127.0.0.1:9221/pve | grep pve_version_info
```

Check output of that command. It should be similar to the following:

```sh
# HELP pve_version_info Proxmox VE version info
# TYPE pve_version_info gauge
pve_version_info{release="7.2",repoid="963997e8",version="7.2-15"} 1.0
```