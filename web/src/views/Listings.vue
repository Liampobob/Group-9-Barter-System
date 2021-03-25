<template>
  <section class="hero is-primary is-fullheight">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-5-tablet is-4-desktop is-3-widescreen">
            <div class="box">
              <ul id="listings">
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

@Options({
  components: {},
  computed: {
    ...mapGetters("listingsStore", ["getListings"]),
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
