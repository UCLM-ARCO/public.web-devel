=============================
Carga asíncrona con AngujarJS
=============================

En este ejemplo los datos NO se encuentran en la página web ni se cargan en la
plantilla. Es el cliente (Angular) quién pide al servidor los datos de los vuelos cuando
se carga la página.

Incorpora algunas diferencias relevantes respecto al anterior:

* Lo anterior implica que el código JS no necesita estar en una plantilla y se puede
  almacenar en el STORE.
* Se ha incorporado un nuevo modelo (``TrackPoint``) para listar los puntos por los que
  pasa el UAV en cada vuelo.
* Los vuelos tienen un nuevo atributo ``status`` que indica el resultado del vuelo según
  la leyenda: OK, FAILURE, ISSUES.
* Todos los métodos tienen un método ``marshable()`` que ofrece una versión serializable
  (como diccionarios) de cada instancia, de modo que puede convertirse directamente a
  JSON.
* Una nueva vista ``/data/`` ofrece acceso directo a la representación JSON del modelo.




Modelos
=======

[``prj/eventlog/models.py``]

.. literalinclude:: ../080-angular-async/prj/eventlog/models.py
   :linenos:


URLS
====

[``prj/prj/urls.py``]

.. literalinclude:: ../080-angular-async/prj/prj/urls.py
   :lines: 16-


[``prj/eventlog/urls.py``]

.. literalinclude:: ../080-angular-async/prj/eventlog/urls.py



Vistas
======

[``prj/eventlog/views.py``]

.. literalinclude:: ../080-angular-async/prj/eventlog/views.py
   :linenos:



Plantillas
==========

La vista debe generar una página como ésta:

.. image:: figures/angular-async.png


[``prj/eventlog/templates/base.html``]

.. literalinclude:: ../080-angular-async/prj/eventlog/templates/base.html
   :language: html
   :linenos:
   :end-before: <!--


[``prj/eventlog/templates/list.html``]

.. literalinclude:: ../080-angular-async/prj/eventlog/templates/event-list.html
   :language: html
   :linenos:
   :end-before: <!--


JavaScript
==========

[``prj/eventlog/static/js/eventlog/app.js``]

.. literalinclude:: ../080-angular-async/prj/eventlog/static/eventlog/js/app.js
   :language: js
   :linenos:


[``prj/eventlog/static/js/eventlog/controllers.js``]

.. literalinclude:: ../080-angular-async/prj/eventlog/static/eventlog/js/controllers.js
   :language: js
   :linenos:


Ejercicios
==========

* Evitar que el modelo se cargue al iniciar la página. Añadir un botón "Refresh" para recargar bajo demanda.
