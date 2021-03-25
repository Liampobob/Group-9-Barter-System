<template>
  <section class="hero is-primary is-fullheight">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-5-tablet is-4-desktop is-3-widescreen">
            <div class="box has-text-centered">
              <!-- <HelloWorld v-bind:msg="getUser" /> -->
              <!-- <button class="button is-primary" v-on:click="changeName()">
                Execute a store action
              </button>
              <button class="button is-primary" v-on:click="call()">Call backend</button> -->
              <button class="button is-secondary" v-on:click="signout()">Sign out</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import HelloWorld from "@/components/HelloWorld.vue";
import { Options, Vue } from "vue-class-component";
import { mapActions } from "vuex";
import axios from "@/shared/axios";

@Options({
  components: {
    HelloWorld,
  },
  computed: {
    getUser() {
      return "test";
      // return this.$store.state.testModule.user;
    },
  },
  methods: {
    // Get action changeName from testModule store
    ...mapActions("testModule", ["changeName"]),
    call: async () => {
      const a = await axios.get("auth_health", {
        headers: { Authorization: `Token ${localStorage.getItem("token")}` },
      });
      console.log(a.data);
    },
  },
})
export default class Home extends Vue {
  signout() {
    this.$store.dispatch("userStore/logout");
  }
}
</script>
