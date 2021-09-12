Instalar y habilitar un entorno virtual, documentación [aqui](https://docs.python.org/es/3/tutorial/venv.html)

Para correr el proyecto y los test primero debe ingresar a la carpeta src del proyecto se debe configurar la siguiente variable de entorno:

`cd <path_project>/src`

`export PYTHONPATH=<path_project>/src`

Instalar requerimientos en el entorno virtual con el siguiente comando:

`pip install -r requirements.txt`

Para correr las pruebas del proyecto usé el siguiente comando:

`python -m unittest`

Si quiere correr el script que realiza la carga a la base de datos se debe correr el archivo import_db.py con el siguiente comando:

`python utils/import_db.py`

Para poder instalar la configuración inicial antes de correr su proyecto ejecuté el siguiente comando:

`python utils/install.py`

Para ejecutar su proyecto debe ejecutar el siguiente comando:

`python app.py`

Tenga en cuenta que la aplicación estará corriendo por **localhost:5000**,
y al momento de realizar el request, en los headers se debe agregar la llave **"X-API-KEY"** con un valor **"123456"**,

Parámetros que acepta el request:

query: Se pueden ingresar filtros y el orden de los datos
page: Número de la página la cual quiere realizar el request por defecto es 1
per_page: Número de registros a traer por página, por defecto es 10, maximo por página 50

Ejemplo request:

http://127.0.0.1:5000/pokemon/?query={"order":{"name":"desc"},"filter":{"name":"Venusaur","legendary":false}}&page=1&per_page=3
