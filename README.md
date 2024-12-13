Disclaimer: URL, passwords and other sensible data committed to this project no
longer exist

---

# URL de la aplicación desarrollada

- Frontend: https://cliente-template-iweb-uma.vercel.app/
- Backend: https://cliente-iweb-uma.fly.dev
- BBDD:
  mongodb+srv://iweb:cliente-iweb-uma-jdsauu2nodau2@cliente-iweb-uma.wpsvwmu.mongodb.net/?retryWrites=true&w=majority

# Tecnologías utilizadas

- Base de datos: Mongodb, alojado en Mongodb Atlas
- Backend: Desarrollado en Python 3.11 y usando FastAPI. Desplegado en fly.io
- Frontend: Desarrollado en TypeScript usando Astro, Svelte y React. Desplegado
  en Vercel
- Oauth2: Proporcionado por Auth0
- Pagos: Paypal
- Subida de imágenes: Cloudinary
- Mapas: Leaflet y OpenStreetMaps

# Instrucciones de instalación y despliegue

El servicio está compuesto de dos componentes (backend y frontend). Para
instrucciones detalladas sobre instalación y despliegue, visite los ficheros
`README.md` disponibles en la carpeta `backend` y `frontend`

# Credenciales

## PayPal sandbox clients

```json
[
  {
    "email": "sb-5qp7q22405408@personal.example.com",
    "password": "2o}yF$ct"
  }
]
```

# Funcionalidad implementada

- Todo lo relacionado con mapas
- Oauth
- Lista de logs: Por alguna razon Auth0 no devuelve los logs con la consulta,
  con un poco más de tiempo podría haberlo extraido

# Otras anotaciones

Nada que añadir
