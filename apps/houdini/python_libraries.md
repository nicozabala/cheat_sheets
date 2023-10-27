Para agregar Python Libraries a Houdini hay dos metodos

## 1. Mediante pip y hython
Se descarga e instala pip para el interprete de houdini
```bash
curl https://bootstrap.pypa.io/get_pip.py -o TARGET_PATH
C:/ProgramFiles/SideFx/Houdini19.x.xx/bin/hython TARGET_PATH
hython -m pip install scipy
```

## 2. Usando la variable de entorno PYTHON_PATH
Se crea una variable de entorno PYTHON_PATH con los paths donde se encuentran las librerias que deseamos cargar.

