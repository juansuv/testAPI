# Test TUSDATO.CO

_Este proyecto esta diseñado para obtener los pokemons directamente de la POKEAPI y mostrarlos en una vista Tambien encontrara un enpoint para realizar un scrapi a una web y guardarlos en un archivo xlsx el cual se asigna el nombre por parametro._

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

_El Proyecto se ejecuta en un entorno virutal de pipenv, entonces es necesario tenerlo instalado en la maquina_

```
pip install pipenv
```

_una vez instalado el entorno virtual procedemos a instalar los requisitos del proyecto los cuales se encuentra en el PIPFILE dentro de la carpeta principal del proyecto_

```
pipenv install
```

_con esto terminanos de instalar los requisistos para que nuestro proyecto funcione_


### Instalación 🔧

_Activamos el entorno virtual que creamos con el comando_


```
pipenv shell
```

_Y corremos nuestro servidor con el siguiente comando_

```
uvicorn main:app --reload
```

_Una vez reaizado esto quedara nuesta aplicacion dispobible en la siguiente direcion_

* [API](http://localhost:8000/pokemon/)

## Ejecutando las pruebas ⚙️

_al principio nuestra base de datos en SQLITE llamada pokemons.db estara vacia. por esto no nos muestra ningun pokemon, para obtenerlos debemos llamar al endpoint /get el cual obtendra los pokemons directamente de la POKE_

* [APIGET](http://localhost:8000/pokemon/get)

_una vez realizado esto obtendremos el listado de todos los pokemos disponibles en la app_

_para realizar la busqueda entre todos los pokemos solo se debe ingresar los caracteres a buscar despues de la url de la siguiente manera_

* [APISEARCH](http://localhost:8000/pokemon/pi)


## Despliegue 📦

_Esta desarrollado para un solo ambiente entonces es de facil despliege_


```
uvicorn main:app --reload
```
## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [FastAPI](https://https://fastapi.tiangolo.com/) - El framework web usado
* [SQLAlchemy](https://https://www.sqlalchemy.org/) - Manejador de Bases de datos


## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/juansuva/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/juansuv/testAPI/wiki)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/juansuv/testAPI/tags).

## Autores ✒️

_desarrollo y diseño_

* **Juan Diego Suarez Vargas** - *Desarrollo y Diseño* - [Juan Suarez](https://github.com/juansuv/)

## Licencia 📄

Este proyecto está bajo la Licencia (GNU) - mira el archivo [LICENSE.md](LICENSE.md) para detalles





---
⌨️ con ❤️ por [Juan Suarez](https://www.linkedin.com/in/juan-diego-suarez-vargas-34a88a183/) 😊