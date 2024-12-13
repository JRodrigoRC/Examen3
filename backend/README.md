# Uso

## Despliegue de la aplicación

La aplicación ha sido diseñada para ser desplegada en fly.io. Para ello, será
necesario tener instalada el CLI `flyctl`

```sh
# Cargar las variables de entorno
cat .env | flyctl secrets import
# Desplegar la aplicación
flyctl deploy
```

## Ejecución de desarrollo

### Requisitos

- Python 3.11 o superior
- Pip3

### Instrucciones

```sh
# Crear un entorno virtual
python -m venv .venv
source .venv/bin/activate
# Instalar los paquetes necesarios
pip install -r requirements.txt

# Configuración necesaria para arrancar el servicio
export mongo_url=<VALOR>
export mongo_collection=<VALOR>
# Ver la sección Configuración ...
# Iniciar el servidor
uvicorn --reload --port 8000 --host 127.0.0.1 src:app
```

## Ejecución mediante docker

```sh
# Compilar el contenedor
docker build -t fastapi-app .
# Inicializar el contenedor. Añadir todas las variables de entorno necesarias
docker run -p 8000:8080 \
    -e mongo_url=<VALOR> \
    -e mongo_collection=<VALOR> \
    -e mongo_database=<VALOR> \
    fastapi-app
```

# Configuración

La aplicación admite las siguientes opciones de configuración mediante ficheros
`.env` o variables de entorno

| Variable             | Descripción                             | Valor por defecto |
| -------------------- | --------------------------------------- | ----------------- |
| `mongo_url`          | URL de un servidor Mongodb              |                   |
| `mongo_collection`   | Colección donde almacenar los datos     |                   |
| `mongo_database`     | Base de datos donde buscar la colección |                   |
| `locationiq_apikey`  | LocationIQ api key                      |                   |
| `locationiq_baseurl` | LocationIQ API URL                      |                   |
| `paypal_clientid`    | Paypal client id                        |                   |
| `paypal_secret`      | Paypal client secret                    |                   |
| `paypal_url`         | Paypal API URL                          |                   |
| `auth_audience`      | JWT audience                            |                   |
| `auth_baseurl`       | Base url where to find public JWK       |                   |

# Documentación

Se proporciona un fichero `openapi.json` con la especificación de OpenApi.
Además, el propio servidor web proporciona la documentación sobre los endpoints
REST bajo las rutas `/docs` (SwaggerUI) y `/redoc` (Redoc)
