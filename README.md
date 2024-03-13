![image](https://github.com/electronicdeivid/djangoLab/assets/162055932/6b5f36ad-e73a-4096-981e-3f9cb6e81c3a)# djangoLab

Documentación de mi experimentación en el django framework. Es tener un respaldo personal, y registro de progreso, más que otra cosa.
La carpeta de proyecto es la carpeta empleado. Las apps de django se alojan en la carpeta applications.
La configuración de la base de datos, se hacen en employee-->settings-->local.py  se configura para trabajar con postgreSQL en mi caso la versión 15.
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

------------HELP ME PLEASE !----------------------------
Actualmente Necesito resolver cómo a un modelo empleado, le asocio distintas skills,del modelo skill. 
He probado con Foreignkey y con ManytoMant, en el primer caso, solo me permite, asociar una skill 
por empleado, a distintos empleados puedo asignarle la misma Skill. Mediante manytomany, se asocian todas 
las skills al empleado, es decir no tengo poder desde el administrador a escoger cuáles se le asocian y cuáles no.
Necesito filtrar del las skills disponibles y asociar las que yo quiera a cada empleado. 


![image](https://github.com/electronicdeivid/djangoLab/assets/162055932/0743508d-0270-40b2-9fdb-e2f34e2e4831)


![image](https://github.com/electronicdeivid/djangoLab/assets/162055932/fc18be00-bf6f-4322-a764-8e95879010aa)

