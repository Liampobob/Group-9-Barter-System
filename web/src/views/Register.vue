<template>
  <div>
    <navbar/>
    <section class="hero is-primary is-fullheight-with-navbar">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-centered">
            <div class="column is-5-tablet is-4-desktop is-3-widescreen">
              <div class="box">
                <div class="field" id="choose_accounttype">
                  <label class="label">Account Type</label>
                  <div class="dropdown">
                    <div class="dropdown-trigger">
                      <button
                        class="button is-fullwidth"
                        aria-haspopup="true"
                        aria-controls="dropdown-menu"
                        @click="setDropdown()"
                      >
                        <span>{{ selectedItem }}</span>
                        <span class="icon is-medium">
                          <i class="fas fa-angle-down" aria-hidden="true"></i>
                        </span>
                      </button>
                      <div
                        class="dropdown-menu"
                        id="dropdown-menu-vfor"
                        role="menu"
                      >
                        <div
                          class="dropdown-content"
                          v-for="a in accountTypes"
                          v-bind:key="a"
                        >
                          <div class="dropdown-item is-fullwidth">
                            <button
                              class="button is-fullwidth is-inverted"
                              @click="
                                () => {
                                  selectedAccount = a;
                                  setDropdown();
                                }
                              "
                            >
                              {{ a }}
                            </button>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <form>
                  <div
                    class="field"
                    id="select_isCBO"
                    v-if="selectedAccount === 'Business'"
                  >
                    <input v-model="isCBO" class="checkbox" type="checkbox" />
                    This business is a Community-Based Organisation
                  </div>
                  <div class="field" id="input_username">
                    <label class="label">Username</label>
                    <div class="control">
                      <input
                        v-model="username"
                        class="input"
                        type="text"
                        placeholder="Username"
                      />
                    </div>
                  </div>
                  <div class="field" id="input_password">
                    <label class="label">Password</label>
                    <div class="control">
                      <input
                        v-model="password"
                        class="input"
                        type="password"
                        placeholder="********"
                      />
                    </div>
                  </div>
                  <div class="field" id="input_name">
                    <label class="label">Name</label>
                    <div class="control">
                      <input
                        v-if="selectedAccount === 'User'"
                        v-model="name"
                        class="input"
                        type="text"
                        placeholder="Full Name"
                      />
                      <input
                        v-if="selectedAccount === 'Business'"
                        v-model="name"
                        class="input"
                        type="text"
                        placeholder="Business Name"
                      />
                    </div>
                  </div>
                  <div class="field" id="input_phonenumber">
                    <label class="label">Phone Number</label>
                    <div class="control">
                      <input
                        v-model="phone"
                        class="input"
                        type="text"
                        placeholder="06..."
                      />
                    </div>
                  </div>
                  <div v-if="selectedAccount === 'Business'">
                    <div class="field" id="input_contactname">
                      <label class="label">Contact Name</label>
                      <div class="control">
                        <input
                          v-model="contactName"
                          class="input"
                          type="text"
                          placeholder="Contact Name"
                        />
                      </div>
                    </div>
                    <div class="field" id="input_worktags">
                      <label class="label">Work Tags</label>
                      <div class="control">
                        <input
                          v-model="workTags"
                          class="input"
                          type="text"
                          placeholder="Electrical, Sewing, ..."
                        />
                      </div>
                    </div>
                  </div>
                  <div id="input_textarea">
                    <div
                      class="field"
                      id="input_bio"
                      v-if="selectedAccount === 'User'"
                    >
                      <label class="label">Bio</label>
                      <div class="control">
                        <textarea
                          v-model="bio"
                          class="input is-fullwidth"
                          type="text"
                          placeholder="Your bio..."
                        />
                      </div>
                    </div>
                    <div
                      class="field"
                      id="input_description"
                      v-if="selectedAccount === 'Business'"
                    >
                      <label class="label">Description</label>
                      <div class="control">
                        <textarea
                          v-model="description"
                          class="input is-fullwidth"
                          type="text"
                          placeholder="Business Description"
                        />
                      </div>
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
                  <div class="is-fullwidth" id="submit_button">
                    <button
                      type="button"
                      class="button is-primary is-fullwidth"
                      @click="register"
                    >
                      Register
                    </button>
                  </div>
                </form>
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
import store from "@/store";
import Navbar from "../components/Navbar.vue";

@Options({
  components: {Navbar},
  computed: {},
})
export default class Register extends Vue {
  accountTypes = ["User", "Business"];
  selectedAccount = "User";
  get selectedItem() {
    return this.selectedAccount;
  }
  set selectedItem(newSelectedItem: string) {
    this.selectedAccount = newSelectedItem;
    this.isBusiness = this.selectedAccount === "Business";
    console.log(this.isBusiness);
    this.setDropdown();
  }
  setDropdown() {
    const dropdown = document.querySelector(".dropdown");
    if (dropdown != null) dropdown.classList.toggle("is-active");
  }

  username = "";
  password = "";
  name = "";
  phone = "";
  bio = "";
  isBusiness = this.selectedAccount === "Business";
  isCBO = false;
  contactName = "";
  workTags = "";
  description = "";

  errors: string[] = [];

  async register() {
    console.log(this);
    this.errors = [];
    if (!this.username) {
      this.errors.push("username cannot be empty");
    }
    if (!this.password) {
      this.errors.push("password cannot be empty");
    }
    if (!this.name) {
      this.errors.push("name cannot be empty");
    }
    if (!this.phone) {
      this.errors.push("phone cannot be empty");
    }

    if (this.errors.length === 0) {
      const username = this.username.trim();
      const password = this.password.trim();
      const name = this.name.trim();
      /* eslint-disable @typescript-eslint/camelcase */
      const phone_number = this.phone.trim();
      const bio = this.bio.trim();
      const is_business = this.selectedAccount === "Business";
      const is_cbo = this.isCBO;
      const contact_name = this.contactName.trim();
      const work_tags = this.workTags.trim();
      const description = this.description;
      const resp = await this.$store.dispatch("userStore/register", {
        username,
        password,
        name,
        phone_number,
        bio,
        is_business,
        is_cbo,
        contact_name,
        work_tags,
        description,
      });
      if (resp && resp["errors"]) {
        this.errors = resp["errors"].includes("403")
          ? ["Username already taken"]
          : ["An error occured"];
      }
    }
  }
}
</script>

<style>
textarea.input {
  height: 200px;
}
</style>
