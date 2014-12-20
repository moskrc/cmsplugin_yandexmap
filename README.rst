===================
cmsplugin_yandexmap
===================

cmsplugin_yandexmap - это плагин для django-cms. Позволяет добавлять на страницу интерактивную Яндекс карту. 
Возможности аналогичны плагину googlemap входящему в состав данной CMS.

Лицензия MIT.

Зависимости
===========

* django-cms >= 3.0

Установка
=========

Как обычно::

    $ pip install cmsplugin_yandexmap

или ::

    $ easy_install cmsplugin_yandexmap

или ::

    $ hg clone http://github.org/moskrc/cmsplugin_yandexmap/
    $ cd cmsplugin_yandexmap
    $ python setup.py install


Добавить плагин в ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'cmsplugin_yandexmap',
        ...
    )

Запустить ``syncdb``, или ``migrate`` если вы используете South.