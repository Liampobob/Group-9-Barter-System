<template>
  <section class="hero is-primary is-fullheight">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-5-tablet is-4-desktop is-3-widescreen">
            <div class="has-text-centered">
              <div class="dropdown is-fullwidth">
                <div class="dropdown-trigger is-fullwidth">
                  <button class="button is-medium is-fullwidth" aria-haspopup="true" aria-controls="dropdown-menu" @click="setDropdown()">
                    <span>{{selectedItem}}</span>
                    <span class="icon is-medium">
                      <i class="fas fa-angle-down" aria-hidden="true"></i>
                    </span>
                  </button>
                </div>
                <div class="dropdown-menu is-fullwidth" id="dropdown-menu" role="menu">
                  <div class="dropdown-content is-fullwidth">
                    <div class="dropdown-item is-fullwidth">
                      <button class="button is-medium is-fullwidth" @click="() => {selectedItem = 'All';}">
                        All
                      </button>
                    </div>
                    <div class="dropdown-item is-fullwidth">
                      <button class="button is-medium is-fullwidth" @click="() => {selectedItem = 'Jobs';}">
                        Jobs
                      </button>
                    </div>
                    <div class="dropdown-item is-fullwidth">
                      <button class="button is-medium is-fullwidth" @click="() => {selectedItem = 'Classes';}">
                        Classes
                      </button>
                    </div>
                    <div class="dropdown-item is-fullwidth">
                      <button class="button is-medium is-fullwidth" @click="() => {selectedItem = 'To Sell';}">
                        To Sell
                      </button>
                    </div>
                    <div class="dropdown-item is-fullwidth">
                      <button class="button is-medium is-fullwidth" @click="() => {selectedItem = 'To Buy';}">
                        To Buy
                      </button>
                    </div>
                  </div>
                </div>
              </div>
              <input ref="searchBar is-large is-rounded  " class="input" type="text" v-model="searchTerms" placeholder="Search for listings">
              <button class="button is-fullwidth is-medium" @click="searchForListings">
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

import { Vue } from "vue-class-component";
import store from "@/store";

export default class Search extends Vue {
  terms = '';
  get searchTerms() {return this.terms;}
  set searchTerms(terms) {this.terms = terms;}

  dropdownItem = 'All';
  get selectedItem() {return this.dropdownItem;}
  set selectedItem(newSelectedItem: string) {this.dropdownItem = newSelectedItem; this.setDropdown()}

  setDropdown() {
    const dropdown = document.querySelector('.dropdown');
    console.log(dropdown);
    if(dropdown != null)
      dropdown.classList.toggle('is-active');
  }

  async searchForListings() {
    // API call to backend to get listings

    //store listing
    store.dispatch("listingsStore/searchListings", {terms: this.terms, category:this.dropdownItem});
  }
}
</script>
