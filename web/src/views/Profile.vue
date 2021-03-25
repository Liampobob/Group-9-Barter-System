<template>
  <div>
    <div class="columns is-mobile is-centered">
      <div class="column is-half">
        <div class="box">
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
