<template>
  <section class="hero is-primary is-fullheight">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-5-tablet is-4-desktop is-3-widescreen">
            <div class="box has-text-centered">
              <div class="" v-if="selectedUser">
            <label class="label">My Profile</label>
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
          </div>
        </div>
      </div>
    </div>
  </section>
</template>


<script lang="ts">
import { Options, Vue } from "vue-class-component";

@Options({
  components: {},
  computed: {
    selectedUser() {
      return this.$store.getters["userStore/user"];
    },
  },
})
export default class MyProfile extends Vue {
  mounted() {
    if (!this.$store.getters["userStore/user"]) {
      this.$store.dispatch("userStore/loadProfile");
    }
  }
}
</script>
