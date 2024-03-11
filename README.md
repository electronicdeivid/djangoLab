# djangoLab

Documentación de mi experimentación en el django framework. Es tener un respaldo personal, y registro de progreso, más que otra cosa.
La carpeta de proyeco es la carpeta empleado. Las apps d edjango se alojan en la carpeta applications.
La configuración de la base de datos, se hacen en empleado-->settings-->local.py  se configura para trabajar con postgreSQL en mi caso la versión 15.
Para ejecutar el proyecto correctamente, se deben tener los siguientes paquetes en un espacio virtual (principalmente sqlparse, y psycopg2 para trabajar con la ORM de django):

Package           Version
----------------- -------
asgiref           3.7.2
Django            4.2.11
pip               21.1.1
psycopg2          2.9.9
setuptools        56.0.0
sqlparse          0.4.4
typing-extensions 4.10.0
tzdata            2024.1
