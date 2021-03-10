<template>
  <section class="hero is-primary is-fullheight">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-5-tablet is-4-desktop is-3-widescreen">
            <div class="has-text-centered">
              <input ref="searchBar is-medium is-rounded  " class="input" type="text" v-model="searchTerms" placeholder="Search for listings">
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
    const tmpListing2 : Listing = {
      title: 'Job2',
      description: 'Description2',
    }
    const tmpListing3 : Listing = {
      title: 'Job3',
      description: 'Description3',
    }
    //store listing
    this.$store.dispatch("listingsStore/setListings", [tmpListing,tmpListing2,tmpListing3]);
  }
}
</script>
