<template>
  <div>
    <div class="columns is-mobile is-centered">
      <div class="column is-half">
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
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { User } from "@/types/User";

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
    this.username = this.$route.params["username"] ?? "";
    if (this.username) {
      var resp = await this.$store.dispatch("userStore/getWorker", {
        username: this.username,
      });
    }
    if (resp?.["error"]) {
      this.error = resp["error"];
    }
  }
}
</script>
