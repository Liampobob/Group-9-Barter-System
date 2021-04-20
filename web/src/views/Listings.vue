<template>
  <section class="hero is-primary is-fullheight">
    <navbar/>
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-5-tablet is-4-desktop is-3-widescreen">
            <div class="box">
              <div class="column">
                <h3>Featured Listing</h3>
              </div>
              <div class="column">
                <button class="button is-fullwidth is-inverted" v-if="getFeaturedListing.title !== ''" @click="() => {openListing(getFeaturedListing.title);}">
                      {{ getFeaturedListing.title }}
                </button>
              </div>
              <ul id="listings">
                <div class="column">
                  <h3>Search Results</h3>
                </div>
                <div v-for="(listing, index) in getListings" :key="listing.title" class="column">
                  <button class="button is-fullwidth is-inverted" @click="() => {openListing(listing.title);}">
                      {{index+1}}: {{ listing.title }}
                  </button>
                </div>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">

import { Options, Vue } from "vue-class-component";
import { mapGetters } from "vuex";
import store from "@/store";
import Navbar from "./Navbar.vue"

@Options({
  components: {Navbar},
  computed: {
    ...mapGetters("listingsStore", ["getListings"]),
    ...mapGetters("listingsStore", ["getFeaturedListing"]),
  },
})
export default class Listings extends Vue {
  openListing(title: string) {
    this.$router.push("/listing/" + title);
  }

  async mounted() {
    const resp = store.getters["listingsStore/getListings"];
    if(resp.length == 0) {
          store.dispatch("listingsStore/searchListings", {terms: "", category:"All"});
    }
}
}
</script>
