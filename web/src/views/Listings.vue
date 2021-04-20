<template>
  <div>
    <navbar/>
    <section class="hero is-primary is-fullheight-with-navbar">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-centered">
            <div class="column is-5-tablet is-4-desktop is-3-widescreen">
              <div class="box">
                <div class="column" v-if="getFeaturedListing.title !==''">
                  <h3>Featured Listing</h3>
                </div>
                <div class="column">
                  <button class="button is-fullwidth is-inverted" v-if="getFeaturedListing.title !== ''" @click="() => {openListing(getFeaturedListing.title);}">
                        {{ getFeaturedListing.title }}
                  </button>
                </div>
                <div class="column" v-if="getListings.length === 0">
                  <h3>No Results Found</h3>
                </div>
                <ul v-if="getListings.length != 0" id="listings">
                  <div class="column">
                    <h3>Results</h3>
                  </div>
                  <div v-for="(listing, index) in getListings" :key="index" class="column">
                    <button class="button is-fullwidth is-inverted" v-if="listing.hasOwnProperty('title')" @click="() => {openListing(listing.title);}">
                        {{index+1}}: {{ listing.title }}
                    </button>
                    <button class="button is-fullwidth is-inverted" v-if="listing.hasOwnProperty('name')" @click="() => {openBusiness(listing.username);}">
                        {{index+1}}: {{ listing.name }}
                    </button>
                  </div>
                </ul>
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
import { mapGetters } from "vuex";
import store from "@/store";
import Navbar from "../components/Navbar.vue"

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
  openBusiness(username: string) {
    this.$router.push("/worker/" + username);
  }
}
</script>
