<script lang="ts">
  import { uploadImageFile } from "../lib/cloudinary";

  export let imageKey = "";
  export let endpointURL = "";

  let files: FileList;
  async function handler(event: any) {
    const formData = new FormData(event.target);
    const uploadResult = await uploadImageFile(files[0]);
    formData.set(imageKey, uploadResult.secure_url);
    const result = await fetch(endpointURL, {
      body: formData,
      method: "POST",
    }).then((x) => x.json());
    window.location.href = result.redirect;
  }
</script>

<form on:submit|preventDefault={handler}>
  <div class="mb-3">
    <label for="formFile" class="form-label">Upload your image</label>
    <input class="form-control" type="file" id="formFile" required bind:files />
  </div>
  <slot />
</form>
