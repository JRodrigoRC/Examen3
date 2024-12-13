# Uso

## Ejecución de desarrollo

### Requisitos

- Node 19+
- npm 8+
- Java JDK 1.8+

### Instrucciones

```sh
# 1. Instalar las dependencias
npm i
# 2. Compilar la api. Se debe de ejecutar en cada cambio en la especificación
npm run openapi
# 3. Iniciar el servidor
npm run dev
```

## Ejecución de producción

La aplicación ha sido configurada para ser desplegada en Vercel para producción,
por lo que no puede ser ejecutada en modo producción localmente. El cliente se
encuentra accesible en https://cliente-template-iweb-uma.vercel.app/

# Configuración

La aplicación admite las siguientes opciones de configuración mediante ficheros
`.env` o variables de entorno

| Variable                          | Descripción                 | Valor por defecto |
| --------------------------------- | --------------------------- | ----------------- |
| `BACKEND_URL`                     | URL del servidor REST       |
| `AUTH0_CLIENTSECRET`              | Client secret de Auth0      |
| `PUBLIC_CLOUDINARY_CLOUD_NAME`    | Cloud name de Cloudinary    |
| `PUBLIC_CLOUDINARY_UPLOAD_PRESET` | Upload preset de Cloudinary |
| `PUBLIC_PAYPAL_CLIENTID`          | Client ID de Paypal         |
| `PUBLIC_AUTH0_CLIENTID`           | Client ID de Auth0          |
| `PUBLIC_AUTH0_BASEURL`            | Base URL del dominio Auth0  |
| `PUBLIC_AUTH0_AUDIENCE`           | Audiencia del dominio Auth0 |
