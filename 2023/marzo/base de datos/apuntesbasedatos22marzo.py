#Consulta de Datos usando Lenguaje Estructurado
#de Consultas

#ésta es una de las
#actividades que con mayor frecuencia se estará realizando sobre la base
#de datos, bien sea a través de un Sistema de Gestión de Bases de Datos
#(SGBD) o desde el lenguaje de programación.

#Las consultas pueden tener diferentes grados de complejidad, desde las

#que extraen la información de una tabla o complementando la informa-
#ción desde diferentes tablas, la incorporación de funciones de tipo esta-
#dístico sobre los datos y la generación de grupos de datos para crear nive-
#les de resumen. Las cuales son implementadas en los sistemas de infor-
#mación a través de las consultas, informes o reportes a generar.

'''Consultar Datos, provenientes de diferentes Tablas'''
#Este tipo de consultas se utiliza frecuentemente, su objetivo es visualizar
#datos que están en diferentes tablas, específicamente los datos de
#aquellas que tienen llaves foráneas.

#En este tipo de consultas se vuelven a trabajar los alias, solo que en esta
#ocasión el alias es para las tablas.

#Sintaxis:
'''SELECT *
FROM <Nombre_tabla1>AS <alias Tabla1> INNER JOIN
<Nombre_tabla2>AS <alias Tabla2>
ON <aliasTabla1>.<Campo_llaveprimaria> =
<aliasTabla2>.<Campo_llaveforánea>'''

#Ejemplo:
'''SELECT PacNombres, PacApellidos, PacSexo, MedNombres,
MedApellidos
FROM Tblpacientes INNER JOIN TblMedicos
ON TblMedicos.MedIdentificacion = Tblpacientes.
PacMedIdentifica'''

#Ejemplo Utilizando alias para las tablas
'''SELECT PacNombres, PacApellidos, PacSexo, MedNombres,
MedApellidos
FROM Tblpacientes as TP INNER JOIN TblMedicos as TM
ON TM.MedIdentificacion = TP. PacMedIdentifica'''

#Nota:
'''tp y tm son los alias de las tablas'''

#Producto cartesiano:
#Consiste en una nueva tabla formada por las filas que resulten de todas
#las combinaciones posibles de las filas de la primera tabla con todas las
#filas de la segunda tabla. El número de filas resultante es el producto de
#la multiplicación de todas las filas de la primera tabla por la segunda. Por
#esta razón es imprescindible adicionar un filtro que corresponda con el
#vínculo que existe entre las tablas, de otra forma los resultados no serían
#coherentes con la información.

#Cuando se realiza una consulta, se especifican en la cláusula SELECT las
#columnas de cada tabla que se desean visualizar, en la cláusula FROM los
#nombres de las tablas que contienen la información separadas por coma.

#Por último en la cláusula WHERE una condición en la cual intervienen al
#menos una columna de cada tabla que representan la conexión entre las
#dos tablas.

#Sintaxis:
'''SELECT *
FROM <Nombre_tabla1> , <Nombre_tabla2>
WHERE <Tabla1>.<Campo> = <Tabla2>.<Campo>'''

#El rendimiento en este tipo de consultas es bajo, ya que sin importar la
#condición que se establezca, se deben combinar (multiplicar) todas las
#filas de una y otra tabla y luego se filtra de acuerdo con la condición.

#Combinaciones
'''Consisten en obtener los registros de las tablas a partir de diferentes tipos
de combinaciones, que están determinadas por el cumplimiento de una
cierta condición entre dos de sus columnas. Se especifica en la cláusula
FROM y se identifica con la palabra JOIN.
Existen diferentes tipos de combinaciones, las cuales se presentan a
continuación:'''

#1.Combinación Interna – INNER JOIN