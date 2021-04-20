<template>
  <div>
      <navbar />
    <div class="hero is-primary is-fullheight-with-navbar">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-centered">
            <div class="column is-half">
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
                    <p>{{ selectedUser.work_tags.split(",").join(", ") }}</p>
                  </div>
                  <div class="field" v-if="selectedUser.working_days">
                    <label class="label">Working Days</label>
                    <p>{{ selectedUser.working_days }}</p>
                  </div>
                  <br />
                  <label class="label">Reviews</label>
                  <div class="control has-icons-left">
                    <input
                      type="number"
                      class="input"
                      max="5"
                      min="1"
                      v-model="stars"
                    />
                    <span class="icon is-small is-left">
                      <i class="fas fa-star"></i>
                    </span>
                  </div>
                  <div v-if="starError">
                    <article class="message is-danger">
                      <div class="message-body">
                        {{ starError }}
                      </div>
                    </article>
                  </div>
                  <div class="control">
                    <textarea
                      v-model="review"
                      class="input is-fullwidth"
                      type="text"
                      placeholder="Your review..."
                    />
                    <div v-if="reviewError">
                      <article class="message is-danger">
                        <div class="message-body">
                          {{ reviewError }}
                        </div>
                      </article>
                    </div>
                  </div>
                  <button
                    class="button is-info is-fullwidth"
                    @click="submitReview"
                  >
                    Submit
                  </button>
                  <div v-if="submitError">
                    <article class="message is-danger">
                      <div class="message-body">
                        {{ submitError }}
                      </div>
                    </article>
                  </div>
                  <div
                    v-for="review of selectedUserReviews"
                    v-bind:key="review.time.toString()"
                  >
                    <br />
                    <div class="message">
                      <div class="message-header">
                        {{ review.user_name }}
                        {{ review.time.toLocaleString("en-US") }}
                        <span>
                          <i class="fas fa-star"></i>{{ review.stars }}
                        </span>
                      </div>
                      <div class="message-body">
                        <div class="content">
                          {{ review.review_text }}
                        </div>
                      </div>
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
    </div>
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
    selectedUserReviews() {
      return this.$store.getters["userStore/selectedUserReviews"];
    },
  },
})
export default class Worker extends Vue {
  username = "";
  error = "";
  review = "";
  stars = 5;
  reviewError = "";
  starError = "";
  submitError = "";

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

  async submitReview() {
    this.reviewError = "";
    this.starError = "";
    this.submitError = "";

    if (!this.review) {
      this.reviewError = "The review field cannot be empty";
    }
    if (!this.stars) {
      this.starError = "The stars field cannot be empty";
    }

    if (!this.reviewError && !this.starError) {
      const stars = this.stars;
      const review = this.review.trim();
      // TODO submit
      const resp = await this.$store.dispatch("userStore/submitReview", {
        business_username: this.username,
        review_text: review,
        stars: stars,
      });
      if (resp?.error) {
        this.submitError = resp.error;
      }
    }
  }
}
</script>
