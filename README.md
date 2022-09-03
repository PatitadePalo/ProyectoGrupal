> Integrantes:
    - Nicolas Rodriguez
    - Osvaldo Cano Vásquez
    - Nicolas Monroy

> Fue desarrollado con:
Python
Django


> Desde la página inicio, podemos acceder a las 3 distintas secciones del Restaurante: 'Platos Principales', 'Postres' y 'Bebidas'; como también podemos iniciar sesión, crear cuenta y buscar un producto.

> Sin iniciar sesión o logueado con un usuario, la vista de la página será solo de los productos, sin la posibilidad de poder editar/eliminar alguno de ellos.


1-Para acceder a la gestión de la página:
    1.1- A través del botón 'Iniciar sesión', loguearse con el superusuario.
    1.2- Una vez logueado, aparecerá el botón 'Agregar comida/bebida' en la parte superior izquierda la pantalla. Haz click ahí para realizar dicha acción.
    1.3- Especificá el tipo de producto que queres agregar (Plato principal, Bebida o Postre).
    1.4- Llená y enviá el formulario con los datos del producto.
    1.5- Una vez creado, se agregará a la base de datos y te redireccionará a la lista de la categoria que hayas creado.

2- En caso de querer editar/eliminar algun producto, deberás ir a 'Platos Principales', 'Bebidas' o 'Postre' segun el producto al que desea acceder (siempre logueado con el superusuario).
    2.1- Para editar, click en el botón 'Editar'.
        2.1.1- Actualizar los campos del formulario (el cuál nos mostrará los datos previamente ingresado al momento de crearlo).
        2.1.2- Click en 'enviar'.
        2.1.3- Una vez modificado, te redireccionará a la lista de la categoria del producto que hayas modificado.
    2.2- Para eliminar, click en el botón 'Eliminar'.
        2.2.1- Click en 'eliminar'.
        2.2.2- Una vez eliminado, te redireccionará a la lista de la categoria del producto que hayas eliminado.

3- Crea una cuenta.
    3.1-Click el botón 'Crear cuenta'.
    3.2-Llena el formulario con tus datos y click en 'Registrate'.
    3.3-Te redireccionara al menu de 'Iniciar sesión'.
    3.4-Inicia sesión ingresando los datos que recién enviaste.

4- Una vez logueado, podrás acceder a tu 'Perfil' desde la esquina superior derecha.
    4.1- Desde aquí, es posible modificar tus datos haciendo click en el botón 'editar'.
    4.2- Actualizar el formulario y click en 'enviar'.

5- Para cerrar sesión, click en el botón 'Cerrar sesión'.

6- Para realizar la búsqueda de un producto.
    6.1- En la esquina superior derecha encontraremos una caja para la búsqueda de productos.
    6.2- Ingresar el texto que queremos buscar y click en 'Buscar'.






<!-- > En la barra superior encontrarás los botones de 'Platos principales', 'Bebidas' , 'Postres' y 'Agregar comida/bebida'.
En cada uno de ellos se encontrará un listado de lo enunciado en su respectivo botón.
Cada elemento cuenta con su respectiva descripción, precio, imagen y si es apto/no apto para celiacos.

> En el botón de 'Agregar comida/bebida' se prodrá crear un plato principal, una bebida o un postre definiendo sus parametros. 
> Una vez creado se agregará a la base de datos y te redireccionará a la lista de la categoria que hayas creado.

> En el botón de 'Buscar' se podrá introducir un texto que se incluya en cualquiera de los 3 menus y te direccionará al producto solicitado. -->
