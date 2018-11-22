# DockerCrawler

Este es un Crawler de código fuente Javascript. En pocas palabras lo que hace es construir un árbol abarcador del folder "src" y después analiza cada archivo involucrado. La información indexada está se guarda en una base de datos mongo y se pueden hacer cuantos queries sean necesarios siempre y cuando se cumpla con las premisas del esquema. 

## Para Comenzar
Este repositorio es una imagen de docker que corre todos los servicios con ayuda de docker compose. 

### Prerequisitos
* Docker

### Correr Programa
Como primer punto es necesario clonar este repositorio.
```
git clone https://github.com/JoseGuzmanZamora/dockercrawler
```

### Detalle Importante
El código fuente de Javascript debe de estar bajo el directorio de dockercrawler/src/ , de lo contrario, no va a funcionar. Además, la comunicación de los archivos debe de ser por medio de expresiones de "require" y todos los archivos referenciados deben de estar en el folder mencionado. 

Después de haber ingresado los archivos, debe de cambiar el path del archivo de origen. Esto se debe de hacer en la variable "archivoyes" en la línea 14 del archivo crawler.py.
```python
archivoyes = <nombre (no debe de especificar el tipo de archivo)>
```

Al cumplir con los detalles mencionados, puede proceder a correr el programa. 
Asegurese de que Docker esté corriendo. En path del proyecto abra una línea de comandos e ingrese:
```
docker-compose up
```

El programa hará el indexado correspondiente y lo guarda en la base de datos de mongo. 

### Queries 
Sin cerrar la línea de comandos en la que se levantaron los servicios, habra otra línea de comandos e ingrese lo siguiente:
```
docker exec -i -t dockercrawler_database_1  bash

mongo
```
Al estar dentro de mongo, ya puede entrar a la base de datos y empezar a hacer queries. 
```
> use crawler 
> db.general.find()
```

## Esquema en Mongo 
El esquema de la base de datos de mongo es relativamente sencillo, solo cuenta con una collección. Cada objeto identificado por el lexer es un documento con información importante. 
```
ejemplo = {
                        "file": <el archivo al que pertenece>,
                        "type": <tipo de identificador>,
                        "name": <nombre>,
                        "value":<valor>,
                        "params": <arreglo con parámetros en caso de ser una función>,
                        "constructor" <booleano para identificar si la clase usa el predeterminado>,
                        "parent": <en caso que sea una clase heredada>,
                        
                    }
```

## Querys de ejemplo

Query para consultar todas las colecciones que contengan tipo *var* en su código fuente:
```CMD
> db.inicio.find({type:'var'}).pretty()
```

Query todas las colecciones que contengan tipo *function* en su código fuente:
```CMD
> db.inicio.find({type:'function'}).pretty()
```

Query todas las colecciones que contengan tipo *class* en su código fuente:
```CMD
> db.inicio.find({type:'class'}).pretty()
```

Query para consultar una archivo en especifico que contenga un tipo de parámetro:

En este caso, haremos un query para obtener todas las variables del file *test2*:
```CMD
> db.inicio.find({file:'test2', type:'var'}).pretty()
```
Query para obtener todas las funciones del file *test2*:
```CMD
> db.inicio.find({file:'test2', type:'functions'}).pretty()

