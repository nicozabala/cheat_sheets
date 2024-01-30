Para agregar un usuario como sudoer, osea que pueda correr comandos con sudo:

```bash
su -
visudo
```

En el editor buscar la linea:
```bash
root    ALL=(ALL:ALL) ALL
```

Y agregar debajo:

```bash
nico    ALL=(ALL:ALL) ALL
```

Para salvar, tipear ":x"
