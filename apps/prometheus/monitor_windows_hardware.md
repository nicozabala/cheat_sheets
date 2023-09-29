Para monitorear stats del hardware desde Windows la mejor opcion que encontre fue OhmGraphite

https://github.com/nickbabcock/OhmGraphite

Hay que agregarlo como servicio 

 ```bash
 .\OhmGraphite.exe install
 .\OhmGraphite.exe start
 ```

 El config default para Prometheus:

 ```xml
 <?xml version="1.0" encoding="utf-8" ?>
<configuration>
  <appSettings>
    <add key="type" value="prometheus" />
    <add key="prometheus_port" value="4445" />
    
    <!-- This is the host that OhmGraphite listens on.
         `*` means that it will listen on all interfaces.
         Consider restricting to a given IP address -->
    <add key="prometheus_host" value="*" />
    <add key="prometheus_path" value="metrics/" /> 
  </appSettings>
</configuration>
 ```

 Y en el prometheus.yml
 ```bash
 global:
  scrape_interval: 15s
scrape_configs:
  - job_name: 'ohmgraphite'
    static_configs:
    - targets: ['10.0.0.200:4445']
 ```

 Para filtrar hardware se agregan al OhmGraphite.exe.config:

```xml
<add key="/cpu/enabled" value="FaLsE" />
<add key="/gpu/enabled" value="false" />
<add key="/motherboard/enabled" value="false" />
<add key="/ram/enabled" value="false" />
<add key="/network/enabled" value="false" />
<add key="/storage/enabled" value="false" />
<add key="/controller/enabled" value="false" />
<add key="/psu/enabled" value="false" />
<add key="/battery/enabled" value="false" />
```

Recordar, reiniciar el servicio.