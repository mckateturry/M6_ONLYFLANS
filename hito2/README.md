Hito 2: Creación de un sitio web responsive con Bootstrap

Descripción
En este proyecto, continuaremos personalizando el sitio web OnlyFlans utilizando Bootstrap para crear un sitio web responsive y atractivo.

Requerimientos
1. Crear una nueva aplicación Django
Inicia una nueva app de Django llamada web dentro del proyecto onlyflans.
Agrega la app web a la lista de aplicaciones instaladas.
Crea una carpeta templates dentro de la app web y añade un archivo index.html con las estructuras <html>, <header>, y <body> que contenga el texto "índice".
Crea 2 copias del archivo index.html, nombradas about.html y welcome.html, reemplazando el texto del <body> por "acerca" y "bienvenido cliente" respectivamente.
2. Habilitar URLs
Configura las rutas para que muestren los textos básicos:
Ruta /: muestra el texto "índice".
Ruta /acerca: muestra el texto "acerca".
Ruta /bienvenido: muestra el texto "bienvenido cliente".
Ejecuta el servidor de desarrollo con python manage.py runserver y captura pantallazos de cada ruta.