================================
Actualización con polling y REST
================================

Este ejemplo es equivalente al anterior (polling sobre un JSON) pero con dos diferentes importantes:

* El backend ofrece sus recursos con REST (django-rest-framework).
* El frontend utilizar el servido ``ngResource`` para hacer las peticiones REST.


Modelos
=======

[``prj/eventlog/models.py``]

.. literalinclude:: ../091-browser-polling-rest/prj/eventlog/models.py
   :linenos:


Serializadores
==============

.. literalinclude:: ../091-browser-polling-rest/prj/eventlog/serializers.py
   :linenos:



URLS
====

[``prj/prj/urls.py``]

.. literalinclude:: ../091-browser-polling-rest/prj/prj/urls.py
   :lines: 16-


[``prj/eventlog/urls.py``]

.. literalinclude:: ../091-browser-polling-rest/prj/eventlog/urls.py



Vistas
======

[``prj/eventlog/views.py``]

.. literalinclude:: ../091-browser-polling-rest/prj/eventlog/views.py
   :linenos:



Plantillas
==========

[``prj/eventlog/templates/base.html``]

.. literalinclude:: ../091-browser-polling-rest/prj/eventlog/templates/base.html
   :language: html
   :linenos:
   :end-before: <!--


[``prj/eventlog/templates/eventlog.html``]

.. literalinclude:: ../091-browser-polling-rest/prj/eventlog/templates/eventlog.html
   :language: html
   :linenos:
   :end-before: <!--


Partials
--------

.. image:: figures/angular-async.png

[``prj/eventlog/static/js/eventlog/partials/list.html``]

.. literalinclude:: ../091-browser-polling-rest/prj/eventlog/static/eventlog/partials/list.html
   :language: html
   :linenos:
   :end-before: <!--


.. image:: figures/insert-new-flight.png

[``prj/eventlog/static/eventlog/partials/insert.html``]

.. literalinclude:: ../091-browser-polling-rest/prj/eventlog/static/eventlog/partials/insert.html
   :language: html
   :linenos:
   :end-before: <!--


JavaScript
==========

[``prj/eventlog/static/eventlog/js/app.js``]

.. literalinclude:: ../091-browser-polling-rest/prj/eventlog/static/eventlog/js/app.js
   :language: js
   :linenos:


[``prj/eventlog/static/eventlog/js/controllers.js``]

.. literalinclude:: ../091-browser-polling-rest/prj/eventlog/static/eventlog/js/controllers.js
   :language: js
   :linenos:


Ejercicio
=========

* Evitar cargar todo el modelo en cada iteración: añadir una vista para comprobar si hay cambios en caso afirmativo, recargar el modelo completo
