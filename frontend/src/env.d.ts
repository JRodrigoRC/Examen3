/// <reference types="astro/client" />
/// <reference types="astro/client" />

interface ImportMetaEnv {
  readonly BACKEND_URL: string;
  readonly AUTH0_CLIENTSECRET: string;

  readonly PUBLIC_CLOUDINARY_CLOUD_NAME: string;
  readonly PUBLIC_CLOUDINARY_UPLOAD_PRESET: string;

  readonly PUBLIC_PAYPAL_CLIENTID: string;

  readonly PUBLIC_AUTH0_CLIENTID: string;
  readonly PUBLIC_AUTH0_BASEURL: string;
  readonly PUBLIC_AUTH0_AUDIENCE: string;
}
