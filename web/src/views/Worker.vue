<template>
  <div class="hero is-primary is-fullheight">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-5-tablet is-4-desktop is-3-widescreen">
            <div class="box">
              <div class="" v-if="selectedUser">
                <div class="field">
                  <label class="label">Name</label>
                  <p>{{ selectedUser.name }}</p>
                </div>
                <div class="field">
                  <label class="label">Username</label>
                  <p>{{ selectedUser.username }}</p>
                </div>
                <div class="field">
                  <label class="label">Phone</label>
                  <p>{{ selectedUser.phone_number }}</p>
                </div>
                <div class="field">
                  <label class="label">Location</label>
                  <p>{{ selectedUser.location?.latitude }}</p>
                  <p>{{ selectedUser.location?.longitude }}</p>
                </div>
                <div class="field">
                  <label class="label">Bio</label>
                  <p>{{ selectedUser.bio }}</p>
                </div>
              </div>
            </div>
            <div v-if="error">
              <article class="message is-danger">
                <div class="message-body">
                  {{ error }}
                </div>
              </article>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";

@Options({
  components: {},
  computed: {
    selectedUser() {
      return this.$store.getters["userStore/selectedUser"];
    },
  },
})
export default class Worker extends Vue {
  username = "";
  error = "";

  async mounted() {
    this.username = (this.$route.params["username"] as string) ?? "";
    let resp;
    if (this.username) {
      resp = await this.$store.dispatch("userStore/getWorker", {
        username: this.username,
      });
    }
    if (resp?.["error"]) {
      this.error = resp["error"];
    }
  }
}
</script>
