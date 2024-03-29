import { createApp } from "vue";
import App from "./App.vue";
import { router } from "./router";
import store from "./store";
import "@/assets/main.scss";

declare global {
  interface Window {
    fbAsyncInit: () => void;
    // eslint-disable-next-line
    FB: any;
  }
}

createApp(App)
  .use(store)
  .use(router)
  .mount("#app");
