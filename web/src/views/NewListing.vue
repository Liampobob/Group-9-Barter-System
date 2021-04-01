<template>
  <section class="hero is-primary is-fullheight">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-5-tablet is-4-desktop is-3-widescreen">
            <form class="box">
              <div class="field" id="input_title">
                <label class="label">Title</label>
                <div class="control">
                  <input
                    v-model="title"
                    class="input"
                    type="text"
                    placeholder="Post Title"
                  />
                </div>
              </div>
              <div class="field">
                <label class="label">Category</label>
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
                          <button class="button is-fullwidth is-inverted" @click="() => {selectedCategory = c; setDropdown();}">
                            {{ c }}
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="field" id="input_description">
                <label class="label">Description</label>
                <div class="control">
                  <textarea
                    v-model="description"
                    class="input is-fullwidth"
                    type="text"
                    placeholder="Description"
                  />
                </div>
              </div>
              <div class="is-fullwidth" id="submit_button">
                <button class="button is-primary is-fullwidth" type="button" v-on:click="submit()">Submit</button>
              </div>
            </form>
            <div class="has-text-centered">
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
export default class NewListing extends Vue {
  title = '';

  categories = [ "Job", "Class", "To Buy", "To Sell", "CBO"];
  selectedCategory = 'Job';
  get selectedItem() {return this.selectedCategory;}
  set selectedItem(newSelectedItem: string) { this.selectedCategory = newSelectedItem; this.setDropdown(); }
  setDropdown() {
    const dropdown = document.querySelector('.dropdown');
    console.log(dropdown);
    if(dropdown != null)
      dropdown.classList.toggle('is-active');
  }

  description = '';
  errors: string[] = [];

  async submit() {
    this.errors = [];
    if (!this.title) {
      this.errors.push("title cannot be empty");
    }
    if (!this.selectedCategory) {
      this.errors.push("category must be selected");
    }
    if (!this.description) {
      this.errors.push("description cannot be empty");
    }

    if (this.errors.length === 0) {
      const title = this.title;
      const category = this.selectedCategory;
      const description = this.description;
      const resp = await store.dispatch("", {
        title,
        category,
        description,
      });
      if (resp && resp["errors"]) {
        this.errors = ["An error occured"];

      }
    }
  }
}

</script>

<style>
  textarea.input {
    height: 200px;
  }
</style>
