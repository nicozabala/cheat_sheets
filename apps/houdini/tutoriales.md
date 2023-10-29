## Tutoriales SideFX

[x] Just Pipeline Things \
 https://www.sidefx.com/tutorials/just-pipeline-things/

En este tutorial explica los packages, startup scripts, python libraries y algunas tools.


## Illume Webinar - Houdini Pipeline Best Practices (Jeff Wagner)
En esta charla Jeff habla de los conceptos de un pipeline tanto para individuos, pequenos estudios o grandes companias. 

Everything is an asset:
- Geometry Files
- HDA
- Materials
- HIP Files
- Cameras
- Light Setups
- Rendered Images
- Composing Files
- LUTs
- Scripts
- Notes, reference images, footage
- Client conversation notes, reviews, postits

```
Cada vez que se modifica un asset, es un nuevo asset, el anterior no deberia perderse, osea un cambio de version.
```

```
Lo bueno de USD es que entiende que los assets evolucionan de departamento en departamento
```

### $HSITE y $JOB son las variables a usar

Para ver como resuelve los path Houdini usar en el shell
```bash
hconfig -ap
```

