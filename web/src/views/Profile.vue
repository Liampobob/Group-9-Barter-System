<template>
  <div>
    <navbar/>
    <section class="hero is-primary is-fullheight-with-navbar">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-centered">
            <div class="column is-5-tablet is-4-desktop is-3-widescreen">
              <div class="box has-text-centered">
                <div v-if="!editing">
                  <div v-if="selectedUser">
                    <div class="message-header">
                      <p>My Profile</p>
                      <button aria-label="delete" @click="edit(true)">
                        <span class="icon is-small">
                          <i class="fas fa-edit"></i>
                        </span>
                        <span>Edit</span>
                      </button>
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
                <div v-if="editing">
                  <div class="message-header">
                    <p>My Profile</p>
                  </div>
                  <div class="field">
                    <label class="label">Name</label>
                    <input
                      class="input"
                      type="text"
                      placeholder="Name"
                      v-model="editedProfile.name"
                    />
                  </div>
                  <div class="field">
                    <label class="label">Username</label>
                    <input
                      class="input"
                      type="text"
                      placeholder="Username"
                      v-model="editedProfile.username"
                    />
                  </div>
                  <div class="field">
                    <label class="label">Phone</label>
                    <input
                      class="input"
                      type="text"
                      placeholder="Phone Number"
                      v-model="editedProfile.phone_number"
                    />
                  </div>
                  <div class="field">
                    <label class="label">Bio</label>
                    <input
                      class="input"
                      type="text"
                      placeholder="Bio"
                      v-model="editedProfile.bio"
                    />
                  </div>
                  <div class="buttons is-centered">
                    <button class="button is-success" @click="saveEditFields()">
                      <span class="icon is-small">
                        <i class="fas fa-check"></i>
                      </span>
                      <span>Save</span>
                    </button>
                    <button
                      class="button is-danger is-outlined"
                      @click="edit(false)"
                    >
                      <span>Cancel</span>
                      <span class="icon is-small">
                        <i class="fas fa-times"></i>
                      </span>
                    </button>
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
      </div>
    </section>
  </div>
</template>


<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { User } from "@/types/User";
import Navbar from "../components/Navbar.vue";

@Options({
  components: {Navbar},
  computed: {
    selectedUser() {
      return this.$store.getters["userStore/user"];
    },
  },
})
export default class MyProfile extends Vue {
  editing = false;
  editedProfile: User | undefined;
  error = "";

  edit(newValue: boolean) {
    this.editedProfile = newValue
      ? { ...this.$store.getters["userStore/user"] }
      : undefined;
    this.editing = newValue;
    this.error = "";
  }

  async saveEditFields() {
    const status = await this.$store.dispatch("userStore/patchUser", {
      username: this.editedProfile!.username,
      name: this.editedProfile!.name,
      bio: this.editedProfile?.bio ?? "",
      phoneNumber: this.editedProfile?.phone_number ?? undefined,
    });
    if (status.error) {
      this.error = "An error occured.";
      return;
    }
    this.editing = false;
    this.editedProfile = undefined;
    this.error = "";
  }

  mounted() {
    if (!this.$store.getters["userStore/user"]) {
      this.$store.dispatch("userStore/loadProfile");
    }
  }
}
</script>
