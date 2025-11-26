# Sistema de Gestión de Inventario y Ventas

### Integrantes del Equipo

  * **Lucas Castineiras**
  * **Carlo Virgilio**

-----

## 📄 Planteamiento del Escenario

Es una tienda emergente de tecnología especializada en hardware de alto rendimiento y accesorios periféricos. Actualmente, la tienda enfrenta problemas operativos debido a la falta de un sistema digital centralizado: el inventario se lleva manualmente, lo que ocasiona errores en los precios y pérdida de información sobre el stock disponible.

El objetivo de este proyecto es desarrollar una solución de software basada en **Programación Orientada a Objetos (POO)** que permita:

1.  Gestionar un inventario heterogéneo (Laptops y Accesorios con características únicas).
2.  Procesar órdenes de compra de múltiples productos (Carrito de compras).
3.  Persistir la información de manera segura (Base de datos en JSON) para que el inventario no se pierda al cerrar el programa.
4.  Generar reportes rápidos de ventas totales por categoría.

El sistema debe ser escalable, permitiendo agregar nuevas categorías de productos en el futuro sin reescribir el código base, y robusto, manejando errores de entrada del usuario sin colapsar.

-----

## ⚙️ Funcionamiento Esperado

El programa se ejecuta como una aplicación de consola interactiva. A continuación se describe el flujo de trabajo y las características técnicas implementadas:

### 1\. Gestión de Inventario (Herencia y Polimorfismo)

El usuario puede dar de alta nuevos productos en el sistema. El sistema distingue entre tipos de productos gracias al polimorfismo:

  * **Laptops:** Requieren ingresar nombre, precio, SKU y **Memoria RAM**.
  * **Accesorios:** Requieren ingresar nombre, precio, SKU y **Tipo de Compatibilidad**.
  * *Validación:* El sistema impide ingresar precios negativos (Encapsulamiento).

### 2\. Procesamiento de Órdenes (Composición)

El sistema permite crear una nueva orden de venta.

  * El usuario selecciona múltiples productos del inventario disponible.
  * Estos productos se agrupan en un objeto `Order` (una orden **contiene** productos).
  * El sistema calcula automáticamente el total a pagar sumando los precios individuales y genera un "recibo" en pantalla.

### 3\. Reportes de Ventas (Colecciones y Diccionarios)

Cada vez que se finaliza una orden, el sistema actualiza un registro interno utilizando **diccionarios**.

  * El usuario puede consultar en cualquier momento cuánto dinero se ha generado separadamente por categoría (Ej: Total Laptops vs. Total Accesorios).

### 4\. Persistencia de Datos (Archivos JSON)

  * **Al iniciar:** El programa busca automáticamente el archivo `inventory.json`. Si existe, reconstruye los objetos (Laptops y Accesorios) para que el usuario continúe donde se quedó.
  * **Al salir:** El programa guarda el estado actual del inventario en el archivo JSON, asegurando que los nuevos productos agregados no se pierdan.

### 5\. Robustez y Manejo de Errores (Excepciones)

El programa cuenta con un bloque de seguridad (`try-except`) que previene el cierre inesperado de la aplicación en los siguientes casos:

  * Ingreso de texto cuando se espera un número (precio o RAM).
  * Intentos de seleccionar un producto que no existe en la lista.
  * Problemas de lectura/escritura en el archivo de base de datos.

-----

## 🛠️ Tecnologías y Conceptos Aplicados

  * **Lenguaje:** Python 3.x
  * **Paradigma:** Programación Orientada a Objetos (POO).
  * **Conceptos Clave:**
      * Abstracción (Clase base `Product`).
      * Herencia (`Laptop` y `Accessory` heredan de `Product`).
      * Polimorfismo (Método `to_dict` adaptado a cada clase).
      * Encapsulamiento (Protección de variables de precio).
      * Composición (La clase `Order` gestiona objetos `Product`).
  * **Manejo de Datos:** Librería `json` estándar.

-----

## 🚀 Instrucciones de Ejecución

1.  Asegúrese de tener los archivos `main.py`, `models.py` y `data_manager.py` en la misma carpeta.
2.  Ejecute el archivo principal desde la terminal:
    ```bash
    python main.py
    ```
3.  Siga las instrucciones del menú interactivo.