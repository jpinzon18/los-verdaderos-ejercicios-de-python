'''Sistema de Gestion de Base de Datos:'''
#Un Sistema de Gestión de Bases de Datos (SGBD), es un conjunto de pro-
#gramas que permiten el almacenamiento, modificación y extracción de la
#información en una base de datos, lo que permite el almacenamiento,
#manipulación y consulta de datos pertenecientes a una base de datos.

#Estos sistemas proporcionan una interfaz que facilita a los usuarios la realización de diferentes actividades sobre los datos.

#Sin embargo las tareas de manipulación de datos se realizan a través del denominado LenguajeEstructurado de consultas (SQL por sus siglas en inglés: StructuredQuery Language).

#Este lenguaje proporciona la manera de acceder directamente a los datos no sólo a través de los lenguajes de programación, sino desde el mismo
#SGBD. En este material encontrará las características principales de este

#lenguaje y la sintaxis para construir estructuras y objetos de datos, insertar datos, modificarlos, borrar información y la estructura de consulta
#básica.

'''Características:'''
#El SQL se comporta como un lenguaje de “alto nivel”, con una estructura declarativa de sentencias que posee una sintaxis particular y estándar.

'''Lenguaje de definición de datos'''
#Conocido como DDL por sus siglas en inglés (Data Definition Language),
#contienen todas las instrucciones relacionadas con la creación,
#modificación y eliminación de objetos de la base de datos, como son la
#base de datos, tabla, índices, vistas, procedimientos, funciones, triggers,
#etc.

'''Lenguaje de manipulación de datos'''
#Se identifica por las siglas DML (Data Manipulation Language), en la cual
#se encuentran las sentencias que permiten manipular los datos a partir de
#sentencias de inserción, modificación, eliminación y consulta de registros
#de datos.

'''Lenguaje de control de datos'''
#Se identifica por las siglas DCL (Data Control Language), y contiene todas
#las sentencias relacionadas con la seguridad de acceso a los datos.

'''Lenguaje de definición de datos - DDL'''
#El lenguaje de definición de datos puede tener algunas variaciones
#respecto al SMBD (Sistema Manejador de Base de Datos) que se utilice
#para manipularlo, sin embargo existe una codificación estándar que nos
#permite identificar una serie de características del lenguaje y las
#sentencias utilizadas en él. A continuación se describe la construcción de
#bases de datos, tablas, la modificación y eliminación de las mismas.

'''Creación de la Base de Datos
La base de datos es la estructura de almacenamiento principal, la
sentencia que se utiliza para su construcción es CREATE. Su sintaxis y
modo de uso genérico es:'''

#Sintaxis:
'''CREATE DATABASE <Nombre de la Base de Datos>'''

#Ejemplo:
'''Para crear la base de datos CITAS, la sentencia sería:
create database citas'''

#Una vez que se ha construido la base de datos, se deben construir las
#tablas en su interior, es decir que debe estar predefinida o seleccionado
#ese espacio de trabajo.
'''La sentencia que se utiliza para establecer como la base de datos activa
es USE, a continuación su sintaxis:
USE <Nombre de la Base de Datos>'''

#Ejemplo:
'''Para realizar actividades con los objetos de la base de datos cita,
debemos dejarla como la base de datos activa:
use citas'''

#Creación de las tablas
#Para construir las tablas que conforman las bases de datos, se utiliza la
#sentencia CREATE TABLE. Con ésta se crea la estructura de la tabla, lo
#cual permite definir las columnas que tiene y definir ciertas restricciones
#que deben cumplir esas columnas.

'''Las restricciones también conocidas como constraints representan
características particulares que tiene una columna y determinan entre
otras, reglas sobre los contenidos, tipos de datos, limites, relación de la
columna con otras columnas, otros registros de la misma tabla o en otras
tablas.'''

#NOT NULL=La columna o campo deberá contener
#         obligatoriamente un valor. Los campos que se
#         encuentran sin ningún tipo de información se
#         denomina campos nulos y se identifican como NULL

#PRIMARY KEY=Esta columna es la que identifica en forma única cada
#            fila de la tabla, se denomina como clave principal o
#            llave primaria.

#UNIQUE=Identifica una columna que no puede tener valores
#       repetidos en toda la tabla.

#DEFAULT=Permite definir un valor preestablecido para esa
#        columna, es decir que si no se insertan datos en ese
#        campo, el sistema almacenará el valor que por
#        defecto se definió.

#CHECK=Corresponde a condiciones que se pueden definir
#      para aceptar o no datos en los campos. Estas reglas
#      pueden referirse a la misma columna, p.e. (edad > 18)
#      o a otras columnas de la misma tabla.

#FOREIGN KEY=Define la llave foránea de la tabla que puede ser un
#            campo o una combinación de ellos y representa el
#            enlace o relación con otras tablas. El valor que se
#            almacena en esta columna debe estar contenido en
#            otra tabla.

#Sintaxis:

'''CREATE TABLE <Nombre_de_la_tabla> (
<Nombre_de_la_columna1> <tipo de dato>
<Restricción>,
<Nombre_de_la_columna2> <tipo de dato>
<Restricción>,
. . .
<Nombre_de_la_columnan> <tipo de dato>
<Restricción>)'''

#1.2.3. Modificaciones a las Tablas
#El comando utilizado es ALTER TABLE, este comando tiene algunos
#atributos que nos permite realizar cambios a una tabla ya creada. Las
#posibles modificaciones a realizar son: adición de nuevas columnas,
#eliminación de columnas, cambio de tipo de dato, adición de constraints
#(restricciones) a las columnas previamente creadas o la eliminación de
#restricciones.

#Sin embargo para proceder a incorporar el cambio el SMBD realiza una
#serie de verificaciones para que estos cambios no afecten los datos
#previamente registrados (si ya existieran) o entren en contravención con
#reglas anteriores. Por ejemplo, para que una columna pueda modificarse
#y convertirse en llave primaria, debe tener la restricción de not null y los
#datos (si los hubiese) no podrían tener valores repetidos.

#En esta sentencia se utilizan expresiones que determinan el tipo de
#cambio a incorporar, de la siguiente forma:

'''• ADD (COLUMN o CONSTRAINT): para agregar columnas o
restricciones
• DROP (COLUMN o CONSTRAINT): para eliminar columnas o
restricciones
• ALTER / MODIFY : para modificar columnas existentes'''

#Sintaxis:

'''ALTER TABLE <Nombre_de_la_tabla>
ADD (COLUMN) <Nombre_de_la_columna> <tipo de dato>
<Restricción>
ADD(CONSTRAINT) <Nombre_restricción> <tipo_restricción>
<texto_restricción>
DROP (COLUMN) <Nombre_ de_la_columna>
DROP (CONSTRAINT) <Nombre_de_la_restricción>'''

#Ejemplo:
#Se requiere agregar una columna a la tabla Medico, para almacenar el
#registro médico del doctor, que es un número de tipo entero y no puede
#repetirse.

'''Alter table TblMedico
Add Column MedRegistro int
Alter table TblMedico
Add Constraint UNIQUE ( MedRegistro)'''

#Eliminación de Tablas

#La sentencia DROP TABLE permite eliminar una tabla, siempre y cuando
#se tengan permisos sobre el objeto, no se encuentre abierta o siendo
#accesada por algún usuario o si al eliminarla se infringe alguna regla. El
#caso más común está relacionado con las llaves foráneas, cuando el
#contenido de una tabla es referenciada por otra a través de las llaves
#foráneas.

#Sintaxis:
'''DROP TABLE <Nombre_de_ la_ tabla>'''

#Ejemplo:

#Si se deseara eliminar la tabla Medico y no existieran referencias de otras
#tablas, la sentencia a utilizar es:
'''Drop table TblMedico'''

# Inserción de datos
#La sentencia INSERT se utiliza para agregar los registros a una tabla, es
#decir que se agregan filas completas de datos a la tabla, previa a la
#inserción se realiza un proceso de verificación de las restricciones
#presentes en cada campo, es decir que si el campo es llave primaria, el
#valor a insertar no sea nulo o repetido y así sucesivamente con cada dato
#a insertar. La fila siempre es agregada al final de la tabla y el valor de
#cada campo debe coincidir con el tipo de dato establecido para cada
#columna.

#Sintaxis:
''''INSERT INTO <Nombre_de_la_tabla> (<Nombre_columna1>,
<Nombre_columna2> <Nombre_columnaN>) VALUES (valor1, valor2,
valorN)'''

#Ejemplo:
#En la tabla Medico se va a insertar los datos del doctor Germán
#Fernández, con identificación 19208547 y registro medico 854632. La
#sentencia de inserción sería:

'''INSERT INTO TblMedico (MedIdentificacion, MedNombres,
MedApellidos, MedRegistro) VALUES (19208547, ‘German’,
‘Fernandez’, 854632)'''

#Los datos de tipo alfanumérico, así como las fechas, generalmente se
#escriben entre comillas simples o dobles dependiendo del SMBD a usar.

''' Modificación de Datos:'''
#La sentencia UPDATE se utiliza para realizar modificaciones sobre los
#datos que se encuentran en los campos de una tabla. El sistema realiza
#una validación de la integridad de los campos, verificando que los nuevos
#datos no infrinjan ninguna de las restricciones asociadas a los campos. Se
#debe tener especial cuidado en proporcionar adecuadamente la condición
#que determina sobre cual o cuales de los registros deben aplicarse los
#cambios.

#Sintaxis:

'''UPDATE <Nombre_de_la_tabla>
SET <Nombre_columna a cambiar valor> = <Nuevo_Valor>
WHERE <condición>'''

#Ejemplo:

#Se desea modificar la dirección de residencia del médico Antonio Mejía, su
#nueva dirección es: “avenida de las flores con calle 23”. La sentencia de
#modificación de datos entonces sería:
'''UPDATE TblMedico
SET MedDireccion = “avenida de las flores con calle 23”'''
#Si se dejara hasta aquí, se modificarían todos las direcciones de los
#médicos, de otro modo al agregar la condición se especifican los registros
#sobre los cuales se debe hacer el cambio.
'''UPDATE TblMedico
SET MedDireccion = “avenida de las flores con calle 23”
WHERE MedNombres = “Antonio” AND MedApellidos = “Mejía”'''

#Más adelante en este material encontrará los aspectos más relevantes a
#considerar para construir los filtros o condiciones de las sentencias SQL.

'''Eliminación de Registros:'''
#La sentencia DELETE se utiliza para borrar filas de datos de una tabla. El
#sistema realiza una validación de la integridad referencial antes de
#ejecutar la acción. Así como con la modificación se debe tener especial
#cuidado en proporcionar adecuadamente la condición que determine cual
#o cuales de los registros deben ser borrados.

#Sintaxis:
'''DELETE
FROM <Nombre_de_la_tabla>
WHERE <condición>'''

#Ejemplo:
#Se desea retirar de la base de datos al médico German Fernandez, con
#registro médico 854632. La sentencia de modificación de datos entonces
#sería:
'''DELETE
FROM TblMedico
WHERE MedNombres = “German” AND MedApellidos = “fernandez” AND
MedRegistro = 854632'''

#Aunque no es necesario proporcionar todos los datos, se debe asegurar
#que la condición filtra únicamente el o los registros que se desean
#eliminar. Se recomienda entonces realizar una consulta previa y utilizar la
#misma condición para filtrarlo posteriormente.

'''Consulta de datos:'''
#Con la sentencia SELECT se visualiza la información de la base de Datos.
#Los datos que se presentan corresponden a una o más filas de una tabla
#o también a una o más filas de una o más tablas.

#La sintaxis básica es:

'''SELECT <Nombre_columna> o <lista de columnas>
FROM <Nombre_de_la_tabla>'''

#Ejemplo:
#Se desea consultar los nombres y apellidos de todos los médicos, la
#sentencia para hacer esta consulta sería:
'''SELECT MedNombres, MedApellidos
FROM TblMedico'''

#Esta instrucción, puede ir acompañada de las siguientes clausulas:
'''WHERE <condición>
GROUP BY <Nombre_columna1>, ...
HAVING <condición>
ORDER BY <Nombre_columna> <Modo de ordenamiento>'''

#Antes de realizar cualquier consulta a la base de Datos, es muy
#importante tener claro cuál o cuáles son los datos que se requiere
#visualizar y de que tabla o tablas se van a extraer.

#En caso de que se deseara consultar TODOS los campos de la tabla, no es
#necesario escribir todos los campos, a menos que se desee escribirlo en
#un orden particular, si no es así se utiliza el comodín * (asterisco) que
#representa todos los campos.

#En el ejemplo anterior se requería solo nombre y apellido, en caso de
#desear visualizar todos los campos de una tabla, utilizando el comodín *,
#quedaría la sentencia de la siguiente manera:

'''Select * From TblMedico;'''

