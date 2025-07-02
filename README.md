# Sistema de Inventario en Python – Programación Orientada a Objetos

Este proyecto implementa un sistema básico de gestión de inventario utilizando Programación Orientada a Objetos (POO) en Python. Permite gestionar productos (agregar, buscar, actualizar, listar) y calcular el valor total del inventario.

## Estructura del Proyecto

El sistema está contenido en un único archivo:

```
sistema_inventario.py
```

Contiene la definición de dos clases principales:

- Producto
- Inventario

Y una interfaz interactiva por consola que permite al usuario utilizar el sistema fácilmente.

## Funcionalidades

### Clase Producto

Atributos:

- nombre (str)
- precio (float, debe ser mayor o igual a 0)
- cantidad (int, debe ser mayor o igual a 0)

Métodos:

- actualizar_precio(nuevo_precio)
- actualizar_cantidad(nueva_cantidad)
- calcular_valor_total()
- __str__() – Representación legible del producto

### Clase Inventario

Atributos:

- productos – lista de objetos Producto

Métodos:

- agregar_producto(producto)
- buscar_producto(nombre)
- calcular_valor_inventario()
- listar_productos()

### Interfaz de Usuario (Menú)

El sistema presenta un menú interactivo con las siguientes opciones:

1. Agregar producto
2. Buscar producto por nombre
3. Listar todos los productos
4. Calcular valor total del inventario
5. Salir

## Validaciones y Manejo de Errores

El sistema incluye manejo de excepciones para casos como:

- Precios negativos o no numéricos
- Cantidades inválidas
- Nombres vacíos
- Tipos de datos incorrectos
- Producto no encontrado

## Ejecución

1. Asegúrate de tener Python 3 instalado.
2. Descarga el archivo `sistema_inventario.py`.
3. Ejecuta el archivo desde la terminal:

```
python sistema_inventario.py
```

4. Sigue las instrucciones del menú para interactuar con el inventario.

## Ejemplo de Uso

```
--- Menú del Sistema de Inventario ---
1. Agregar producto
2. Buscar producto por nombre
3. Listar todos los productos
4. Calcular valor total del inventario
5. Salir
Ingrese una opción: 1
Ingrese nombre del producto: Lapiz
Ingrese precio del producto: 0.5
Ingrese cantidad del producto: 100
Producto agregado correctamente.
```

## Autor

Desarrollado para la asignatura de Programación Orientada a Objetos en Pytho
