<template>
  <div>
    <navbar/>
    <section class="hero is-primary is-fullheight-with-navbar">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-centered">
            <div class="column is-5-tablet is-4-desktop is-3-widescreen">
              <div class="box">
                <div class="" v-if="selectedUser">
                  <div class="field">
                    <label class="label">Account Type</label>
                    <p>{{ selectedUser.is_business ? "Business" : "User" }}</p>
                    <p v-if="selectedUser.is_cbo">
                      <br />
                      This business is a community based organisation
                    </p>
                  </div>
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
                  <div
                    class="field"
                    v-if="
                      selectedUser.location?.latitude ||
                      selectedUser.location?.longitude
                    "
                  >
                    <label class="label">Location</label>
                    <p>{{ selectedUser.location?.latitude }}</p>
                    <p>{{ selectedUser.location?.longitude }}</p>
                  </div>

                  <div class="field" v-if="selectedUser.contact_name">
                    <label class="label">Contact Person</label>
                    <p>{{ selectedUser.contact_name }}</p>
                  </div>
                  <div class="field" v-if="selectedUser.bio">
                    <label class="label">Bio</label>
                    <p>{{ selectedUser.bio }}</p>
                  </div>
                  <div class="field" v-if="selectedUser.description">
                    <label class="label">Business Description</label>
                    <p>{{ selectedUser.description }}</p>
                  </div>
                  <div class="field" v-if="selectedUser.start_time">
                    <label class="label">Opening Hour</label>
                    <p>{{ selectedUser.start_time }}</p>
                  </div>
                  <div class="field" v-if="selectedUser.end_time">
                    <label class="label">Closing Hour</label>
                    <p>{{ selectedUser.end_time }}</p>
                  </div>
                  <div class="field" v-if="selectedUser.work_tags">
                    <label class="label">Associated Tags</label>
                    <p>{{ selectedUser.work_tags.split(',').join(', ') }}</p>
                  </div>
                  <div class="field" v-if="selectedUser.working_days">
                    <label class="label">Working Days</label>
                    <p>{{ selectedUser.working_days }}</p>
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
    </section>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import Navbar from "../components/Navbar.vue";

@Options({
  components: { Navbar },
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
