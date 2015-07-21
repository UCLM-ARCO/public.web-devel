========================================
Lectura asíncrona con AngularJS con REST
========================================

Este ejemplo demuestra cómo realizar la lectura asíncrona del modelo desde el cliente
mediante una consulta REST.


[``prj/eventlog/static/eventlog/js/app.js``]

.. literalinclude:: ../081-angular-async-rest/prj/eventlog/static/eventlog/js/app.js
   :language: js

El servicio Angular para invocaciones REST se llama ``ngResource``. Su uso se puede ver en
el fichero ``controllers.js``.


[``prj/eventlog/static/eventlog/js/controllers.js``]

.. literalinclude:: ../081-angular-async-rest/prj/eventlog/static/eventlog/js/controllers.js
   :language: js


Plantillas
==========

La vista debe generar una página como ésta:

.. image:: figures/angular-async.png


[``prj/eventlog/templates/base.html``]

.. literalinclude:: ../081-angular-async-rest/prj/eventlog/templates/base.html
   :language: html
   :linenos:
   :end-before: <!--
   :emphasize-lines: 18


[``prj/event_list/templates/list.html``]

.. literalinclude:: ../081-angular-async-rest/prj/eventlog/templates/event-list.html
   :language: html
   :linenos:
   :end-before: <!--
   :emphasize-lines: 42


URLS
====

[``prj/prj/urls.py``]

.. literalinclude:: ../081-angular-async-rest/prj/prj/urls.py
   :lines: 16-


[``prj/eventlog/urls.py``]

.. literalinclude:: ../081-angular-async-rest/prj/eventlog/urls.py


Se han incluido vistas REST para todos los modelos:

[``prj/eventlog/serializers.py``]

.. literalinclude:: ../081-angular-async-rest/prj/eventlog/serializers.py

[``prj/eventlog/views.py``]

.. literalinclude:: ../081-angular-async-rest/prj/eventlog/views.py


Importante no olvidar añadir la aplicación ``rest_framework`` en el ``settings.py``::

  INSTALLED_APPS = (
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',

      'eventlog',
      'rest_framework',
  )


Ejercicio
=========

Hacer recarga explícita mediante un botón "Refresh" como en el ejercicio anterior, pero usando REST.
