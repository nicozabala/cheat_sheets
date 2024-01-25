Primero hay que descargar lo siguiente:
Windows:
	- Visual Studio Community 2023
	- CMake (Este no estoy seguro si fue necesario)
	- Python 3.9.13 (CHEQUEAR bien la version en https://github.com/PixarAnimationStudios/OpenUSD/blob/release/VERSIONS.md )
	- Desde pip, instalar PyOpenGL, PySide6

Descargar el source desde https://github.com/PixarAnimationStudios/OpenUSD o usando git
```bash
git clone https://github.com/PixarAnimationStudios/OpenUSD
```

Correr el script que compila y descarga todas las dependencias:
```bash
C:\> python USD\build_scripts\build_usd.py "C:\USD"
```

Si llega a fallar el download de boost, reemplazar lineas 730 a 737 del build_usd.py
```python
    if context.buildPython and pyVer >= (3, 10):
        BOOST_URL = "https://archives.boost.io/release/1.78.0/source/boost_1_78_0.zip"
    elif IsVisualStudio2022OrGreater():
        BOOST_URL = "https://archives.boost.io/release/1.78.0/source/boost_1_78_0.zip"
    elif MacOS():
        BOOST_URL = "https://boostorg.jfrog.io/artifactory/main/release/1.78.0/source/boost_1_78_0.zip"
    else:
        BOOST_URL = "https://archives.boost.io/release/1.78.0/source/boost_1_78_0.zip"
```

**Agregar las System Environment Variables como dice al final del compilado**

Para hacer que usdedit abra los archivos en otro editor distinto al default, en Windows hay que agregar una variable de entorno USD_EDITOR con el path del editor.

Ojo porque en particular Houdini lee tambien PYTHONPATH y al ser de otra version de Python, esto genera errores. Lo comprobe limpiando la env PYTHONPATH y asi funciona el Hou en 3.10 cuando USD es 3.9, me queda ver como hacer para que co-existan ambos entornos.