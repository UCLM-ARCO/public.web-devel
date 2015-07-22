=========================================
Representación de datos con Google Charts
=========================================

En este ejemplo usaremos Google Charts para representar algunos datos de los UAV a partir de la lista de vuelos.

Los cambios más importantes son:

* Se ha creado un nuevo "partial" para mostrar los datos de un UAV concreto (que debe incluirse en el router de Angular)
* Se ha creado un controlador Angular para esa nueva vista, que incluye la mayor parte del código para utilizar Google Charts
* Una nueva vista para obtener los datos de un UAV específico desde el backend.


Modelos
=======

[``prj/eventlog/models.py``]

.. literalinclude:: ../130-google-charts/prj/eventlog/models.py
   :linenos:


URLS
====

[``prj/prj/urls.py``]

.. literalinclude:: ../130-google-charts/prj/prj/urls.py
   :lines: 16-


[``prj/eventlog/urls.py``]

.. literalinclude:: ../130-google-charts/prj/eventlog/urls.py



Vistas
======

[``prj/eventlog/views.py``]

.. literalinclude:: ../130-google-charts/prj/eventlog/views.py
   :linenos:



Plantillas
==========

[``prj/templates/base.html``]

.. literalinclude:: ../130-google-charts/prj/templates/base.html
   :language: html
   :linenos:
   :end-before: <!--


[``prj/eventlog/templates/eventlog.html``]

.. literalinclude:: ../130-google-charts/prj/eventlog/templates/eventlog.html
   :language: html
   :linenos:
   :end-before: <!--


Partials
--------

.. image:: figures/angular-async.png

[``prj/eventlog/static/js/eventlog/partials/list.html``]

.. literalinclude:: ../130-google-charts/prj/eventlog/static/eventlog/partials/list.html
   :language: html
   :linenos:
   :end-before: <!--


.. image:: figures/insert-new-flight.png

[``prj/eventlog/static/eventlog/partials/insert.html``]

.. literalinclude:: ../130-google-charts/prj/eventlog/static/eventlog/partials/insert.html
   :language: html
   :linenos:
   :end-before: <!--



[``prj/eventlog/static/eventlog/partials/uav.html``]

.. literalinclude:: ../130-google-charts/prj/eventlog/static/eventlog/partials/uav.html
   :language: html
   :linenos:
   :end-before: <!--


JavaScript
==========

[``prj/eventlog/static/eventlog/js/app.js``]

.. literalinclude:: ../130-google-charts/prj/eventlog/static/eventlog/js/app.js
   :language: js
   :linenos:


[``prj/eventlog/static/eventlog/js/controllers.js``]

.. literalinclude:: ../130-google-charts/prj/eventlog/static/eventlog/js/controllers.js
   :language: js
   :linenos:


Gunicorn
========

Para poder utilizar WebSocket Django debe ejecutarse con un servidor de WSGI. Por ese motivo se utiliza ``Gunicorn``. El modo más sencillo es crear el siguiente fichero:

[``prj/wsgi.py``]

.. literalinclude:: ../130-google-charts/prj/prj/wsgi.py
   :linenos:

El servidor se ejecuta con::

  $ gunicorn --reload -k prj.wsgi.Worker prj.wsgi


Ejercicio
=========

* Cambia el tipo de gráfico para "traveled distance" a "scatter chart"
* Añade un "range filter" a modo de slider para hacer zoom en el gráfico.
