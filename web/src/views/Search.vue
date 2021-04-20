<style>
  .dropdown {
  width: 100%;
  }
  .dropdown-trigger {
    width: 100%;
  }
  .dropdown-menu {
  width: 100%;
  }
  .dropdown-content {
    width: 100%;
  }
  .dropdown-item {
    width: 100%;
  }
</style>


<template>
  <section class="hero is-primary is-fullheight">
    <navbar/>
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-5-tablet is-4-desktop is-3-widescreen">
            <div class="has-text-centered">
              <div class="dropdown">
                <div class="dropdown-trigger">
                  <button class="button is-fullwidth" aria-haspopup="true" aria-controls="dropdown-menu" @click="setDropdown()">
                    <span>{{ selectedItem }}</span>
                    <span class="icon is-medium">
                      <i class="fas fa-angle-down" aria-hidden="true"></i>
                    </span>
                  </button>
                  <div class="dropdown-menu" id="dropdown-menu-vfor" role="menu">
                    <div class="dropdown-content" v-for="c in categories" v-bind:key="c">
                      <div class="dropdown-item is-fullwidth">
                        <button class="button is-fullwidth is-text" @click="() => {selectedCategory = c; setDropdown();}">
                          {{ c }}
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <input ref="searchBar is-large is-rounded  " class="input" type="text" v-model="searchTerms" placeholder="Search for listings">
              <button class="button is-fullwidth" @click="searchForListings">
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

import { Options, Vue } from "vue-class-component";
import store from "@/store";
import Navbar from "./Navbar.vue";

@Options({
  components: {Navbar},
  computed: {},
})
export default class Search extends Vue {
  terms = '';
  get searchTerms() {return this.terms;}
  set searchTerms(terms) {this.terms = terms;}

  categories = [ "All", "Businesses", "Jobs", "Classes", "To Buy", "To Sell", "CBOs"];
  selectedCategory = 'All';
  get selectedItem() {return this.selectedCategory;}
  set selectedItem(newSelectedItem: string) {this.selectedCategory = newSelectedItem; this.setDropdown()}

  setDropdown() {
    const dropdown = document.querySelector('.dropdown');
    console.log(dropdown);
    if(dropdown != null)
      dropdown.classList.toggle('is-active');
  }

  async searchForListings() {
    store.dispatch("listingsStore/searchListings", {terms: this.terms, category:this.selectedCategory});
  }
}
</script>
