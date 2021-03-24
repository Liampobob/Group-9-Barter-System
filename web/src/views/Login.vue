<template>
  <section class="hero is-primary is-fullheight">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-5-tablet is-4-desktop is-3-widescreen">
            <div class="box has-text-centered">
              <div class="field">
                <label class="label">Username</label>
                <div class="control has-icons-left">
                  <input
                    class="input"
                    type="text"
                    placeholder="Username"
                    v-model="username"
                  />
                  <span class="icon is-small is-left">
                    <i class="fas fa-user"></i>
                  </span>
                </div>
              </div>
              <div class="field">
                <label class="label">Password</label>
                <div class="control has-icons-left">
                  <input
                    class="input"
                    type="password"
                    placeholder="Password"
                    v-model="password"
                  />
                  <span class="icon is-small is-left">
                    <i class="fas fa-key"></i>
                  </span>
                </div>
              </div>
              <div v-if="errors.length" class="mb-3">
                <article class="message is-danger">
                  <div class="message-header">
                    <p v-for="error of errors" v-bind:key="error">
                      {{ error }}
                    </p>
                  </div>
                </article>
              </div>
              <div class="buttons are-medium">
                <button class="button is-grey" @click="login">
                  <i class="fas fa-sign-in-alt mr-1"></i>
                  Login
                </button>
              </div>
              <div class="buttons are-medium">
                <button class="button is-info" @click="logInWithFacebook">
                  <i class="fab fa-facebook-f mr-1"></i>
                  Login with Facebook
                </button>
              </div>
              <p class="help is-danger is-size-6">{{ error?.error }}</p>
              <router-link class="has-text-link" :to="{ path: '/register' }"
                >Register</router-link
              >
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

@Options({
  components: {},
  computed: {
    ...mapGetters("userStore", ["error", "token"]),
  },
})
export default class Login extends Vue {
  username = "";
  password = "";
  errors: string[] = [];

  async login() {
    this.errors = [];
    if (!this.username) {
      this.errors.push("username cannot be empty");
    }
    if (!this.password) {
      this.errors.push("password cannot be empty");
    }
    if (this.errors.length === 0) {
      const username = this.username.trim();
      const password = this.password.trim();
      this.$store.dispatch("userStore/auth", { username, password });
    }
  }

  async logInWithFacebook() {
    window.FB.login(
      function (response: any) {
        if (!response.authResponse) {
          this.$store.dispatch("userStore/errorLogin");
          return;
        }
        this.$store.dispatch("userStore/fbLogin", response.authResponse);
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
      // uncomment to enable
      // window.FB.getLoginStatus(function (response: any) {
      //   if (response.authResponse) {
      //     this.$store.dispatch("userStore/fbLogin", response.authResponse);
      //   }
      // });
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
    if (this.$store.getters["userStore/isLoggedIn"]) {
      // Redirect to home if user is logged in.
      this.$router.push("/");
    }
    await this.loadFacebookSDK(document, "script", "facebook-jssdk");
    await this.initFacebook();
  }
}
</script>
