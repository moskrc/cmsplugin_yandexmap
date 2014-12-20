from setuptools import setup, find_packages

version='1.3.2'

setup(
    name = 'cmsplugin_yandexmap',
    version = version,
    author = 'Vitaliy Shishorin',
    author_email = 'moskrc@gmail.com',
    url = 'http://github.com/moskrc/cmsplugin_yandexmap/',
    download_url = 'http://github.com/moskrc/cmsplugin_yandexmap/archive/master.zip',
    description = 'Plugin for django-cms. Yandex Map.',
    license = 'MIT license',
    requires = ['django (>=1.5)','django_cms (>=3.0)'],

    packages=find_packages(),
    package_data={'cmsplugin_yandexmap': ['templates/cmsplugin_yandexmap/*']},


    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: Russian',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    include_package_data=True,
    zip_safe = False,
    install_requires=['django-cms>=3.0',],
)
