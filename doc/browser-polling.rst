=========================
Actualización con polling
=========================

En este ejemplo, se realiza una consulta periódica (polling) del JSON ofrecido por el servidor (que
representa el modelo en el backend) para actualizar el modelo en el frontend. Gracias al
*data binding* de Angular, los cambios son inmediatamente representados en la tabla.

Otros cambios relevantes son:

* Se incorpora el sistema de rutas de Angular (similar a los habituales en los backend). El router se configura por medio del servicio Angular $routerProvider en el fichero ``app.js``.
* El router permite aplicar plantillas parciales (fragmentos de página) en función de la URI.
* Para probar que el *polling* funciona se ha creado un formulario (plantilla ``partials/insert.html``) que mediante el controlador ``EventLogInsertCtrl`` añade un nuevo vuelo al modelo remoto mediante ``post``.
* Para que el formulario que maneja y envía Angular sea aceptado por Django (token CSRF) es necesario ajustar la configuración mediante el ``$httpProvider`` (fichero ``app.js``).
* Se ha incluido un menú con Bootstrap para acceder a las dos vistas disponible: lista e inserción.


Modelos
=======

[``prj/eventlog/models.py``]

.. literalinclude:: ../090-browser-polling/prj/eventlog/models.py
   :linenos:


URLS
====

[``prj/prj/urls.py``]

.. literalinclude:: ../090-browser-polling/prj/prj/urls.py
   :lines: 16-


[``prj/eventlog/urls.py``]

.. literalinclude:: ../090-browser-polling/prj/eventlog/urls.py



Vistas
======

[``prj/eventlog/views.py``]

.. literalinclude:: ../090-browser-polling/prj/eventlog/views.py
   :linenos:



Plantillas
==========





[``prj/eventlog/templates/base.html``]

.. literalinclude:: ../090-browser-polling/prj/eventlog/templates/base.html
   :language: html
   :linenos:
   :end-before: <!--


[``prj/eventlog/templates/eventlog.html``]

.. literalinclude:: ../090-browser-polling/prj/eventlog/templates/eventlog.html
   :language: html
   :linenos:
   :end-before: <!--


Partials
--------

.. image:: figures/angular-async.png

[``prj/eventlog/static/js/eventlog/partials/list.html``]

.. literalinclude:: ../090-browser-polling/prj/eventlog/static/eventlog/partials/list.html
   :language: html
   :linenos:
   :end-before: <!--


.. image:: figures/insert-new-flight.png

[``prj/eventlog/static/eventlog/partials/insert.html``]

.. literalinclude:: ../090-browser-polling/prj/eventlog/static/eventlog/partials/insert.html
   :language: html
   :linenos:
   :end-before: <!--


JavaScript
==========

[``prj/eventlog/static/eventlog/js/app.js``]

.. literalinclude:: ../090-browser-polling/prj/eventlog/static/eventlog/js/app.js
   :language: js
   :linenos:


[``prj/eventlog/static/eventlog/js/controllers.js``]

.. literalinclude:: ../090-browser-polling/prj/eventlog/static/eventlog/js/controllers.js
   :language: js
   :linenos:


Ejercicio
=========

* Evitar cargar todo el modelo en cada iteración: añadir una vista para comprobar si hay cambios en caso afirmativo, recargar el modelo completo
