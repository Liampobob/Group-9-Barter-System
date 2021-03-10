<template>
  <section class="hero is-primary is-fullheight">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-5-tablet is-4-desktop is-3-widescreen">
            <ul id="listings">
              <div v-for="(listing, index) in getListings" :key="listing.title" class="content">
                <h1>{{index+1}}: {{ listing.title }}</h1>
                <h3>{{ listing.description }}</h3>
              </div>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">

import { Options, Vue, Component } from "vue-class-component";
import { mapGetters } from "vuex";
import { Listing } from "@/types/Listing";
@Options({
  components: {},
  computed: {
    ...mapGetters("listingsStore", ["getListings"]),
  },
})
@Component
export default class Listings extends Vue {

  searchForListings() {
    // API call to backend to get listings

    const tmpListing : Listing = {
      title: this.terms,
      description: this.terms,
    }
    console.log(tmpListing);
    //store listing
    this.$store.dispatch("listingsStore/setListings", []);
  }
}
</script>
