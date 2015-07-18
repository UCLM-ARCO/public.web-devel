========
API REST
========

En este ejemplo vamos a crear una interfaz REST para manipular las instancias del modelo Vehicle con el módulo ``djangorestframework``.


Modelos
=======

Recuperamos el modelo sin clave ajena:

.. literalinclude:: ../060-rest/prj/app/models.py
   :linenos:


Serializadores
==============

.. literalinclude:: ../060-rest/prj/app/serializers.py
   :linenos:


URLS
====

En este ejemplo usamos ``urlpatterns`` jerárquicos:

[``prj/prj/urls.py``]

.. literalinclude:: ../060-rest/prj/prj/urls.py
   :lines: 16-
   :linenos:

[``prj/app/urls.py``]

.. literalinclude:: ../060-rest/prj/app/urls.py
   :lines: 16-
   :linenos:


Vistas
======

.. literalinclude:: ../060-rest/prj/app/views.py
   :linenos:

Además django-rest-framework genera vistas autodocumentadas si se accede por medio del navegador. Prueba ``/vehicle/api/``.


Cliente REST
============

Es sencillo hacer un cliente REST con el módulo ``requests``:

[``rest-client.py``]

.. literalinclude:: ../060-rest/rest-client.py
   :linenos:
