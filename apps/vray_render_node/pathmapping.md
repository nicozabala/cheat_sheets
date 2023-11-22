Para hacer path mapping en vray para poder usar el DR en OS mixtos por ejemplo:

-**remapPathFile**="remapFile.xml" – Specifies path to an XML file with path remapping data. Alternatively, the VRAY_PATH_REMAP_FILEPATH environment variable can be used to specify the path to the XML file (see the V-Ray Standalone Environment Variables page for more information). Example file:

```xml
<RemapPaths>
    <RemapItem>
        <From>Z:/export</From>
        <To>/mnt/export</To>
    </RemapItem>
</RemapPaths>
```