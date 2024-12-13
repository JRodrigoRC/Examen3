export interface Eager {
  transformation: string;
  width: number;
  height: number;
  url: string;
  secure_url: string;
}

export interface CloudinaryResponse {
  asset_id: string;
  public_id: string;
  version: number;
  version_id: string;
  signature: string;
  width: number;
  height: number;
  format: string;
  resource_type: string;
  created_at: Date;
  tags: any[];
  pages: number;
  bytes: number;
  type: string;
  etag: string;
  placeholder: boolean;
  url: string;
  secure_url: string;
  access_mode: string;
  original_filename: string;
  eager: Eager[];
}

export async function uploadImageFile(file: File): Promise<CloudinaryResponse> {
  const uploadPreset = import.meta.env.PUBLIC_CLOUDINARY_UPLOAD_PRESET;
  const cloudName = import.meta.env.PUBLIC_CLOUDINARY_CLOUD_NAME;
  const formData = new FormData();
  formData.append("upload_preset", uploadPreset);
  formData.append("file", file);
  return await fetch(
    `https://api.cloudinary.com/v1_1/${cloudName}/image/upload`,
    {
      method: "POST",
      body: formData,
    }
  ).then((x) => x.json());
}
