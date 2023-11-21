
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

a = np.array([1, 2, 3, 4, 5])
```
- Tipo de un objeto
```py
type(a)
```
- Conocer la cantidad de elementos
```py
a.size
```
- Conocer la dimensión
```py
a.ndim
```
- Conocer los tipos de datos almacendos
```py
a.dtype
```
- Conocer las dimenciones y el número de elementos
```py
np.shape
```

## Operaciones
- Suma, Resta, Multiplicación, División
```py
a + 10
a - 10
a * 10
a / 10
```

```py
b = np.array([6, 7, ,8 ,9, 10])

a + b
a - b
a * b
a / b
```

## Tipos de datos

- Almacenar valores según su tipo
```py
a = np.array([6, 7, ,8 ,9, 10], dtype=float)
a = np.array([6, 7, ,8 ,9, 10], dtype=str)
a = np.array([6, 7, ,8 ,9, 10], dtype=bool)
a = np.array([6, 7, ,8 ,9, 10], dtype=np.complex)
```

## Crear arreglos

```py
a = np.arange(0, 100)
a = np.arange(0, 100, 2)
a = np.zeros(10)
a = np.zeros(10, dtype=int)
a = np.ones(10)
a = np.ones(10, dtype=int)
a = np.empty(10)
a = np.empty(10, dtype=int)
a = np.random.randint(0, 100, 50)
```

## Obtener y actualizar elementos

```py
a = np.random.randint(0, 100, 50)

a[0]
a[1]

a[-1]
a[-2]

a[0] = 100
a[-1] = 200
```

## SubArreglos
```py
a = np.random.randint(0, 100, 50)

# a[start:end:saltos]
a[0:5]
a[:5]

a[5:]
a[5::2]

a[[0, 1, 3]]

"""
Para obtener elementos a partir de boleanos, 
estos deben tener el mismo tamaño
"""
a[[True, False, False, False, True]]
```

## Vectorizar funciones
```py
a = np.random.randint(0, 10, 20)

def operacion(valor):
    return (valor ** 2) + 2

operacion(3)
for el in a:
    print(operacion(el))

vector = np.vectorize(operacion)
vector(a)

vector = np.vectorize(lambda valor: (valor ** 2) + 2)
vector(a)
```

## Copias y vistas
```py
import numpy as np

# Copias
a = np.random.randint(0, 10, 20)
b = a.copy()

id(a)
id(b)

a is b

# Vistas
c = a.view()
d = a[:]

id(a)
id(c)
id(c.base)

a is c
a is c.base
```

## Matrices (Arreglos multidimencional)
```py
import numpy as np

A = np.array([
    [1, 2, 3, 4, 5],
    [10, 20, 30, 40, 50],
    [100, 200, 300, 400, 500]
])

A.ndim
A.shape

# A[axi0][axi1] o A[axi0, axi1]
A[0][0]
A[1][2]
A[2][-1]

A[0, 0]
A[1, 2]
A[2, -1]

# Valores de columnas
A[:, 3]
A[[0, 1], 3]
```

## Métodos de agregación
```py
import numpy as np

A = np.array([
    [1, 2, 3, 4, 5],
    [10, 20, 30, 40, 50],
    [100, 200, 300, 400, 500]
])

# Desviación Estandar, Suma, Mínimo, Máximo, Promedio
A.std()
A.sum()
A.min()
A.max()
A.mean()

A[1].sum()
```

## Transposición
```py
import numpy as np

A = np.array([
    [1, 2, 3, 4, 5],
    [10, 20, 30, 40, 50],
    [100, 200, 300, 400, 500]
])

A.T.shape

A[:, 4].sum()
A.T[4].sum()
```

## Filtros y condiciones
```py
import numpy as np

a = np.random.randint(0, 100, 50)
a > 50
a[a > 50]
a[(a > 50) & (a < 90)]
a[(a == 10) | (a == 20) | (a == 50)]
```

## Condiciones
```py
import numpy as np

A = np.array([
    [1, 2, 3, 4, 5],
    [10, 20, 30, 40, 50],
    [100, 200, 300, 400, 500]
])

np.all(A > 50)
np.any((A >= 0) & (A <= 100))
np.any(A > 10)
```

## Funciones Where y Select
```py
import numpy as np

# Where
calificaciones = np.random.randint(1, 11, 10)

np.where(
    calificaciones >= 7,
    'Felicidades, aprobaste la materia.',
    'Lo sentimos, no aprobaste la materia.'
)

# Select
condiciones = [
    (calificaciones == 10),
    ((calificaciones == 8) | (calificaciones == 9)),
    (calificaciones == 7),
    (calificaciones < 7)
]

opciones = [
    'Felicidades, aprobaste la materia con 10',
    'Felicidades, aprobaste la materia',
    'Aprobaste la materia',
    'Lo sentimos no aprobaste la materia'
]

np.select(condiciones, opciones)
```

## Crear y leer archivos pt1
```py
import numpy as np

a = np.random.randint(0, 10, 10)

# Crear
np.savetxt('arreglo.txt', a)
np.savetxt('arreglo.txt', a, fmt='%i')

%load arreglo.txt

# Leer
np.loadtxt('arreglo.txt')
np.loadtxt('arreglo.txt', dtype=int)

# Crear un nuevo arreglo a partir de otro array
c = a.reshape((2, 5))

np.savetxt('matriz.csv', c, delimiter=',', fmt='%i')
%load matriz.csv

# Leer
np.loadtxt('arreglo.txt', delimiter=',', dtype=int)
```

## Crear y leer archivos pt2
```py
import numpy as np

a = np.random.randint(0, 10, 10)

# Crear
np.save('arreglo_binario.npy', a)

# Leer
b = np.load('arreglo_binario.npy')
```

## Modificar arreglos
```py
import numpy as np

a = np.random.randint(0, 10, 10)

# insert
a = np.insert(a, 0, 200)

# append
a = np.append(a, 200)

# delete
a = np.delete(a, -1)

# resize
a = np.riseze(a, 5)

# concatenate
b = np.array([10, 20, 30, 40, 50])
c = np.concatenate([a, b])
```

## Ordenamiento
```py
import numpy as np

a = np.random.randint(0, 10, 20)

# Ascendente
a.sort()

# Descendente
a = a[::-1]

b = np.random.randint(0, 10, 20)

# Ascendente
np.sort(b)

# Descendente
c = np.sort(b)[::-1]
```

# Modulo 3: Pandas

## Series
```py
import pandas as pd

a = pd.Series([1, 2, 3, 4, 5])

# Conocer el tamaño de la serie
a.size

# Conocer el tipo de datos de la serie
a.dtype

# Conocer la dimensión de la serie
a.shape

# Conocer los indices de la serie
a.index

b = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
b['a']

c = pd.Series(
    [1, 2, 3, 4, 5], 
    index=['a', 'b', 'c', 'd', 'e'], 
    name='Números'
)

d = pd.Series(
    [1, 2, 3, 4, 5], 
    index=['a', 'b', 'c', 'd', 'e'], 
    name='Números',
    dtype=int # float, bool, str
)
```

## Clear Series
```py
import pandas as pd

colores = {
    'rojo': 100,
    'verde': 200,
    'azul': 300,
    'negro': 400
}

a = pd.Series(colores)
a['rojo']
```

## Valores núlos
```py
import pandas as pd
import numpy as np

np.nan

a = pd.Series([1, 2, np.nan, np.nan, 5, 6, 7, np.nan, 8, 9])

# isnull
a.isnull()
a[a.isnull()]

# notnull
a.notnull()
a[a.notnull()]
```

## DataFrame pt1

## DataFrame pt2

## Columnas del DataFrame