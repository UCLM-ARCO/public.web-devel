=============
Web framework
=============

Es fácil encontrar una estructura y patrones habituales cuando se crea un servidor web
siguiendo la pauta del ejemplo anterior. Aprovechando esa situación ha surgido
innumerables frameworks para desarrollo de servidores (o aplicaciones) web.

.. image:: figures/web-framework.png


"Hello World" con bottle
========================

Bottle es uno de esos framework, que destaca por su simplicidad y que nos permite abordar algunos conceptos habituales.

.. literalinclude:: ../010-bottle-hello/hello.py
   :linenos:

Para ejecutar este ejemplo se necesita::

  $ sudo apt-get install python-bottle  # debian/ubuntu

o::

  $ sudo pip install bottle


Este servidor incluye varios componentes interesantes que aparecen de forma recurrente:

* Un **controlador** en forma de una función llamada ``hello``. El controlador debe crear
  una página web como resultado y devolver una respuesta HTTP (response).

* Una **ruta** por medio del decorador ``@route`` con la expresión ``/hello/<name>``. De
  este modo el servidor puede determinar que cualquier URL que corresponda con esa
  *expresion regular* implicará la ejecución del controlador.

* Una **vista** generada a partir de una **plantilla** que permite reutilizar el *texto*
  de una página web incorporando el valor de determinadas variables que se substituyen por
  medio de palabras clave ('name' en este caso).


Ejercicios
==========

* Añade al ejemplo un nuevo manejador para "/" que únicamente incluye un enlace para acceder a "/hello".

* Añade al ejemplo un nuevo manejador para "/profile" que presente el perfil de un usuario
  (dado su nombre). Utiliza una plantilla que genere un HTML válido.
