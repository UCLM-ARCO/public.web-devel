========================
"Hello world" con Django
========================

Django es otro framework web, el que vamos a utilizar principalmente en los siguientes ejemplos. Django es sensiblemente más complejo que bottle aunque también mucho más potente.

Toda servidor Django está formado por al menos un **proyecto** y una **aplicación**. Django proporciona una utilería llamada ``django-admin`` que ayuda a generar los ficheros necesarios:

.. code-block:: sh

   $ django-admin startproject hello_prj
   $ cd hello_prj
   $ django-admin startapp hello_app

   $ tree
   ├── hello_app
   │   ├── admin.py
   │   ├── __init__.py
   │   ├── migrations
   │   │   └── __init__.py
   │   ├── models.py
   │   ├── tests.py
   │   └── views.py
   ├── hello_prj
   │   ├── __init__.py
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   └── manage.py


Veamos cómo crear una aplicación equivalente a la anterior en bottle con Django.

Lo primero es registrar el patrón para las URL según una expresión regular.

[``hello_prj/hello_prj/urls.py``]

.. literalinclude:: ../020-django-hello/hello_prj/hello_prj/urls.py
   :lines: 16-


Y crear el controlador (*vista* en la terminología de Django).

[``hello_prj/hello_app/views.py``]

.. literalinclude:: ../020-django-hello/hello_prj/hello_app/views.py


Y un pequeño ``Makefile`` para arrancar el servidor cómodamente:

[``Makefile``]

.. literalinclude:: ../020-django-hello/Makefile

Por último, un pequeño test automática para comprobar que funciona como se espera (fichero ``hello_prj/hello_app/tests.py``):

[``hello_prj/hello_app/tests.py``]

.. literalinclude:: ../020-django-hello/hello_prj/hello_app/tests.py


Ejercicios
==========

* Añade una nueva vista que devuelva que presente el perfil de un usuario (dado su nombre). Utiliza una plantilla que genere un HTML válido completo
