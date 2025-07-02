class Producto:
    """
    Representa un producto dentro del sistema de inventario.

    Attributes:
        nombre (str): Nombre del producto.
        precio (float): Precio unitario del producto.
        cantidad (int): Cantidad disponible del producto.
    """

    def __init__(self, nombre: str, precio: float, cantidad: int):
        """
        Inicializa un producto con nombre, precio y cantidad, validando los datos.

        Args:
            nombre (str): Nombre del producto (no vacío).
            precio (float): Precio del producto (mayor o igual a 0).
            cantidad (int): Cantidad del producto (entero mayor o igual a 0).

        Raises:
            ValueError: Si algún dato es inválido.
        """
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        if not isinstance(precio, (int, float)) or precio < 0:
            raise ValueError("El precio debe ser un número no negativo.")
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un número entero mayor o igual a cero.")

        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio):
        """
        Actualiza el precio del producto.

        Args:
            nuevo_precio (float): Nuevo precio (no negativo).

        Raises:
            ValueError: Si el nuevo precio es inválido.
        """
        if not isinstance(nuevo_precio, (int, float)) or nuevo_precio < 0:
            raise ValueError("El nuevo precio debe ser un número no negativo.")
        self.precio = float(nuevo_precio)

    def actualizar_cantidad(self, nueva_cantidad):
        """
        Actualiza la cantidad disponible del producto.

        Args:
            nueva_cantidad (int): Nueva cantidad (entero no negativo).

        Raises:
            ValueError: Si la nueva cantidad es inválida.
        """
        if not isinstance(nueva_cantidad, int) or nueva_cantidad < 0:
            raise ValueError("La nueva cantidad debe ser un número entero mayor o igual a cero.")
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self):
        """
        Calcula el valor total del producto (precio * cantidad).

        Returns:
            float: Valor total del producto.
        """
        return self.precio * self.cantidad

    def __str__(self):
        """
        Devuelve una representación legible del producto.

        Returns:
            str: Descripción del producto.
        """
        return f"Producto(nombre='{self.nombre}', precio={self.precio}, cantidad={self.cantidad})"


class Inventario:
    """
    Clase que gestiona una colección de productos.
    """

    def __init__(self):
        """
        Inicializa el inventario con una lista vacía de productos.
        """
        self.productos = []

    def agregar_producto(self, producto: Producto):
        """
        Agrega un producto al inventario.

        Args:
            producto (Producto): Objeto producto a agregar.

        Raises:
            TypeError: Si el argumento no es una instancia de Producto.
        """
        if not isinstance(producto, Producto):
            raise TypeError("El producto debe ser una instancia de la clase Producto.")
        self.productos.append(producto)

    def eliminar_producto(self, nombre: str):
        """
        Elimina un producto del inventario por su nombre.

        Args:
            nombre (str): Nombre del producto a eliminar.

        Raises:
            ValueError: Si el nombre es inválido o no se encuentra el producto.
        """
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre del producto no puede estar vacío.")
        
        for i, producto in enumerate(self.productos):
            if producto.nombre == nombre.strip():
                del self.productos[i]
                return
        raise ValueError(f"Producto con nombre '{nombre}' no encontrado en el inventario.")

    def buscar_producto(self, nombre: str):
        """
        Busca un producto por su nombre.

        Args:
            nombre (str): Nombre del producto a buscar.

        Returns:
            Producto | None: El producto encontrado o None si no existe.

        Raises:
            ValueError: Si el nombre es inválido.
        """
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre del producto no puede estar vacío.")

        for producto in self.productos:
            if producto.nombre == nombre.strip():
                return producto
        return None

    def calcular_valor_inventario(self):
        """
        Calcula el valor total del inventario.

        Returns:
            float: Suma del valor total de todos los productos.
        """
        return sum(producto.calcular_valor_total() for producto in self.productos)

    def listar_productos(self):
        """
        Lista todos los productos del inventario.

        Returns:
            str: Representación de todos los productos o mensaje si está vacío.
        """
        if not self.productos:
            return "El inventario está vacío."
        return "\n".join(str(producto) for producto in self.productos)


def menu_principal(inventario):
    """
    Función de interfaz de usuario que permite operar el sistema de inventario.

    Args:
        inventario (Inventario): Instancia del inventario sobre el que se trabaja.
    """
    while True:
        print("\n--- Menú del Sistema de Inventario ---")
        print("1. Agregar producto")
        print("2. Buscar producto por nombre")
        print("3. Listar todos los productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")

        opcion = input("Ingrese una opción: ")

        try:
            if opcion == "1":
                nombre = input("Ingrese nombre del producto: ")
                precio = float(input("Ingrese precio del producto: "))
                cantidad = int(input("Ingrese cantidad del producto: "))
                producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(producto)
                print("Producto agregado correctamente.")

            elif opcion == "2":
                nombre = input("Ingrese el nombre del producto a buscar: ")
                try:
                    producto = inventario.buscar_producto(nombre)
                    if producto:
                        print(producto)
                    else:
                        print("Producto no encontrado.")
                except ValueError as e:
                    print(f"Error: {e}")

            elif opcion == "3":
                print("\nInventario actual:")
                print(inventario.listar_productos())

            elif opcion == "4":
                total = inventario.calcular_valor_inventario()
                print(f"Valor total del inventario: ${total:.2f}")

            elif opcion == "5":
                print("Saliendo del sistema.")
                break

            else:
                print("Opción no válida. Intente nuevamente.")

        except ValueError as ve:
            print(f"Error de entrada: {ve}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    inventario = Inventario()
    menu_principal(inventario)
# Si se ejecuta este archivo directamente, se inicializa el inventario y se muestra el menú principal.
# Si se importa como módulo, no se ejecuta el menú automáticamente.