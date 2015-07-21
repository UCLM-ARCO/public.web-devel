==================
CRUD con ModelForm
==================

En este ejemplo se utiliza una especialización de la clase ``Form`` llamada ``ModelForm``
que conoce el modelo al que representa y simplifica la creación de las vistas.


Modelos
=======

Sin cambios respecto al ejemplo anterior

[``prj/app/models.py``]

.. literalinclude:: ../051-crud-ModelForm/prj/app/models.py
   :linenos:


Formularios
===========

Mediante la clase ``Meta`` se le indica al formulario:

* model: el modelo que representa.
* fields: los campos del modelo que debe incluir.
* widgets: cómo se leerán/representará cada campo.

[``prj/app/forms.py``]

.. literalinclude:: ../051-crud-ModelForm/prj/app/forms.py
   :linenos:

El atributo ``year`` se sobreescribe dado que es necesario pasar los atributos ``min_value`` y ``max_value`` al ``forms.IntegerField``.


Vistas
======

En este ejemplo la vista ``vehicle_update()`` se ha cambiado por una clase (que hereda de la clase ``django.views.generic.View``. Esto permite separar en distintos métodos el comportamiento de GET y POST.

.. literalinclude:: ../051-crud-ModelForm/prj/app/views.py
   :linenos:

Esto también cambia la forma en la que se indica ``urlpatterns``:

[``prj/prj/urls.py``]

.. literalinclude:: ../051-crud-ModelForm/prj/prj/urls.py
   :lines: 16-


Plantillas
==========

.. literalinclude:: ../051-crud-ModelForm/prj/app/templates/base.html
   :language: html
   :linenos:
   :end-before: <!--

.. literalinclude:: ../051-crud-ModelForm/prj/app/templates/vehicle-edit.html
   :language: html
   :linenos:

.. literalinclude:: ../051-crud-ModelForm/prj/app/templates/vehicle-list.html
   :language: html
   :linenos:

.. literalinclude:: ../051-crud-ModelForm/prj/app/templates/vehicle-file.html
   :language: html
   :linenos:


Fixtures
========

.. literalinclude:: ../051-crud-ModelForm/prj/app/sample_data.json
   :language: json
   :linenos:


Tests
=====

El test ``test_list_items()`` utiliza un módulo para creación de `ObjectMother's  <http://martinfowler.com/bliki/ObjectMother.html>`_ llamado `factory boy <https://factoryboy.readthedocs.org/en/latest/>`_. Permite generar automáticamente contenido para la base de datos. Mientras que las *fixtures* son instancias concretas en la base de datos (con todos sus campos especificados), las *ObjectMother's* se puede parametrizar o incluso generar a partir de datos aleatorios.

factory-boy utiliza a su vez un módulo llamado `fake-factory <https://pypi.python.org/pypi/fake-factory>`_ que también se puede utilizar para generar datos de distinto tipo: nombres, direcciones, texto, etc.

.. literalinclude:: ../051-crud-ModelForm/prj/app/tests.py
   :linenos:


Ejercicio
=========

* Añade un nuevo modelo ``Brand``. Añade una vista para crear *marcas*. Utiliza ese nuevo modelo con ``ForeignKey`` en el campo ``Vehicle.brand``.
