
# Modulo 2: iPython
#3 Comandos mágicos

Todos los comandos mágicos empiezan con un `%`.

- Directorio actual de trabajo
```py
%pwd
```
- Navegar entre directorios
```py
%cd
```
- Listar objetos en un directorio
```py
%ls
```
- Almacenar directorios para facilitar su acceso
```py
%pwd
%bookmark {NAME_BOOKMARK}
%bookmark -l
%cd -b {NAME_BOOKMARK}
```
- Almacenar variables
```py
cody = 'Cody'
%store {NAME_VARIABLE}
%store -r
```
- Listar todos los comandos magicos disponibles
```py
%lsmagic
```

## Instrospección de código
Permite conocer mas en profundidad un objeto, puede ser, una clase, un método, una función, una variable, etc. 
```py
{OBJETO}?
```
Para conocer el código que almacena la función:
```py
{OBJETO}??
```

## Manipulación de archivos
- Conocer el contenido del archivo
```py
%cat {NAME_FILE}
```
- Ejecutar el archivo
```py
%run {NAME_FILE}
```
- Cargar un archivo
```py
%load {NAME_FILE}
```
- Conocer la documentación de una función
```py
%pdoc {NAME_FILE}
```
- Editar un archivo
```py
%edit {NAME_FILE}
```

## Crear archivos
```py
%save {NAME_FILE} {BLOQUE_LINEAS} {BLOQUE_LINEAS}
%save -a {NAME_FILE} {BLOQUE_LINEAS} {BLOQUE_LINEAS}
```

# Modulo 3: Numpy

## Arreglos
- Crear un arreglo
```py
import numpy as np

np.array
```