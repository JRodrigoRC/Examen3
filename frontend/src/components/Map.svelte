<script lang="ts">
  // window is undefined (thanks leaflet :D)
  //import L from "leaflet";
  import "leaflet/dist/leaflet.css";

  interface Point {
    coordinates: [number, number];
    text: string;
    open: any;
  }
  export let points: Point[] = [];
  export let origin: [number, number] = [0, 0];
  export let height: undefined | string = "40vh";
  export let width: undefined | string = undefined;

  async function setupMap(htmlElement: HTMLElement) {
    const L = await import("leaflet");
    const map = L.map(htmlElement).setView(origin, 13);

    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      maxZoom: 19,
    }).addTo(map);

    points.forEach(({ coordinates, text, open }) => {
      const marker = L.marker(coordinates).addTo(map).bindPopup(text);
      if (open) marker.openPopup();
    });
  }
</script>

<figure
  use:setupMap
  style:height
  style:width
  class={$$props.class}
  style={$$props.style}
/>
