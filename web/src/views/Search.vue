<template>
  <section class="hero is-primary is-fullheight">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-5-tablet is-4-desktop is-3-widescreen">
            <div class="has-text-centered">
              <input ref="searchBar is-medium is-rounded  " class="input" type="text" v-model="searchTerms" placeholder="Search">
              <button class="button default-login" @click="searchForListings">
                Search
              </button>

            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">

import { Vue, Component } from "vue-class-component";
import { Listing } from "@/types/Listing";

@Component
export default class Search extends Vue {
  terms = '';

  get searchTerms() {return this.terms;}

  set searchTerms(terms) {this.terms = terms;}

  async searchForListings() {
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
