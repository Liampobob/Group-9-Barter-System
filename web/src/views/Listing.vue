<template>
  <section class="hero is-primary is-fullheight">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-5-tablet is-4-desktop is-3-widescreen">
              <div class="box">
                  <h1>Title: {{theListing.title}}</h1>
                  <h3>Description: {{theListing.description}}</h3>
              </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">

import { Options, Vue } from "vue-class-component";
import { Listing } from "@/types/Listing";
import store from "@/store";
@Options({
  components: {},
  computed: {},
})
export default class Listings extends Vue {
    title = '';
    error = '';
    listing: Listing = {title: '', description: ''};

    get theListing() {return this.listing;}
  
    async mounted() {
        this.title = (this.$route.params["title"] as string) ?? "";
        let resp;
        if (this.title) {
            resp = store.getters["listingsStore/getListings"];
        }
        if (resp?.["error"]) {
        this.error = resp["error"];
        }
        for(const listing of resp) {
            if(listing.title == this.title) {
                this.listing = listing;
            }
        }
    }
}
</script>
