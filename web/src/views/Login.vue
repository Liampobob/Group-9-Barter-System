<template>
  <section class="hero is-primary is-fullheight">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-5-tablet is-4-desktop is-3-widescreen">
            <div class="has-text-centered">
              <button class="button is-info" @click="logInWithFacebook">
                <i class="fab fa-facebook-f mr-1"></i>
                Login with Facebook
              </button>
              <p class="help is-danger is-size-6">{{ error?.error }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
// Typescript behaves weirdly with the Facebook JS SDK
/* eslint-disable */

import { Options, Vue } from "vue-class-component";
import { mapGetters } from "vuex";
import store from "@/store";
@Options({
  components: {},
  computed: {
    ...mapGetters("userStore", ["error"]),
  },
})
export default class Login extends Vue {
  async logInWithFacebook() {
    window.FB.login(
      function (response: any) {
        if (!response.authResponse) {
          store.dispatch("userStore/errorLogin");
          return;
        }
        store.dispatch("userStore/login", response.authResponse);
      },
      { scope: "email" }
    );
    return false;
  }

  async initFacebook() {
    window.fbAsyncInit = function () {
      window.FB.init({
        appId: "774102783534474", //You will need to change this
        cookie: true, // This is important, it's not enabled by default
        version: "v9.0",
        autoLogAppEvents: true,
        xfbml: true,
      });

      // Automatically log the user in from Facebook if the facebok login session is still open
      window.FB.getLoginStatus(function (response: any) {
        if (response.authResponse) {
          store.dispatch("userStore/fbLogin", response.authResponse);
        }
      });
    };
  }

  async loadFacebookSDK(d: any, s: any, id: any) {
    var js,
      fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {
      return;
    }
    js = d.createElement(s);
    js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
  }

  async mounted() {
    await this.loadFacebookSDK(document, "script", "facebook-jssdk");
    await this.initFacebook();
  }
}
</script>
