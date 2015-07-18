================
Vistas genéricas
================

Partiendo del ejercicio del ejemplo anterior, se aplican aquí vistas genéricas en los casos en los que resulta conveniente. Para la creación de marcas (brand) se utiliza una CBV  que implementa el método POST.


Modelos
=======

(Sin cambios)

.. literalinclude:: ../052-crud-generic-views/prj/app/models.py
   :linenos:


Formularios
===========

(Sin cambios)

.. literalinclude:: ../052-crud-generic-views/prj/app/forms.py
   :linenos:


Vistas
======

En este caso se utilizan las clases ListView, CreateView y UpdateView que se paremetrizan con:

* model
* template_name
* form_class
* slug_name: El nombre del parámetro capturado en la URI
* success_url: La URI a la que se redirecciona si el formulario tiene éxito.


.. literalinclude:: ../052-crud-generic-views/prj/app/views.py
   :linenos:


URLS
====

.. literalinclude:: ../052-crud-generic-views/prj/prj/urls.py
   :lines: 16-
   :linenos:



Plantillas
==========

.. literalinclude:: ../052-crud-generic-views/prj/app/templates/base.html
   :language: html
   :linenos:
   :end-before: <!--

.. literalinclude:: ../052-crud-generic-views/prj/app/templates/vehicle-edit.html
   :language: html
   :linenos:

.. literalinclude:: ../052-crud-generic-views/prj/app/templates/vehicle-list.html
   :language: html
   :linenos:

.. literalinclude:: ../052-crud-generic-views/prj/app/templates/vehicle-file.html
   :language: html
   :linenos:


Fixtures
========

.. literalinclude:: ../052-crud-generic-views/prj/app/sample_data.json
   :language: json
   :linenos:


Tests
=====

.. literalinclude:: ../052-crud-generic-views/prj/app/tests.py
   :linenos:


Ejercicio
=========

* Muestra un listado resumido de las marcas disponibles bajo el formulario de creación de marcas. Utiliza la vista genérica ``ListView``.
