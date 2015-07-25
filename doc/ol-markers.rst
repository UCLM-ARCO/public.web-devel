==================
OpenLayers markers
==================

En este ejemplo se muestra cómo utilizar "overlays" y marcadores sobre un canvas OpenLayers.


URLS
====

(sin cambios)

[``prj/prj/urls.py``]

.. literalinclude:: ../151-ol-markers/prj/prj/urls.py
   :lines: 16-


[``prj/maps/urls.py``]

.. literalinclude:: ../151-ol-markers/prj/maps/urls.py


Vistas
======

[``prj/maps/views.py``]

.. literalinclude:: ../151-ol-markers/prj/maps/views.py
   :linenos:


Plantillas
==========

[``prj/templates/base.html``]

.. literalinclude:: ../151-ol-markers/prj/templates/base.html
   :language: html
   :linenos:
   :end-before: <!--



[``prj/maps/templates/maps.html``]

.. literalinclude:: ../151-ol-markers/prj/maps/templates/maps.html
   :language: html
   :linenos:
   :end-before: <!--


JavaScript
==========

[``prj/maps/static/maps/js/app.js``]

.. literalinclude:: ../151-ol-markers/prj/maps/static/maps/js/app.js
   :language: js
   :linenos:



[``prj/maps/static/maps/js/controllers.js``]

.. literalinclude:: ../151-ol-markers/prj/maps/static/maps/js/controllers.js
   :language: js
   :linenos:


Ejercicio
=========

* Dado un vuelo cualquiera, mostrar en el mapa los puntos registrados y su recorrido
