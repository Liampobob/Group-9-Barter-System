<template>
  <section class="hero is-primary is-fullheight">
    <div class="hero-body">
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
        <div class="field" id="select_category">
          <label class="label">Category</label>
          <div class="control">
            <select v-model="selected_category">
              <option v-for="c in categories" :value="c.value" v-bind:key="c.value">
                {{ c.text }}
              </option>
            </select>
          </div>
        </div>
        <div class="field" id="input_description">
          <label class="label">Description</label>
          <div class="control">
            <input
              v-model="description"
              class="input"
              type="text"
              placeholder="Description"
            />
          </div>
        </div>
        <div class="button" id="submit_button">
          <button type="button" v-on:click="submit()">Submit</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { Listing } from "@/types/Listing";
import store from "@store";
@Options({
  components: {},
  computed: {},
})
export default class NewListing extends Vue {
  title = '';
  categories = Object[] = [
    { value: 'J', text: "Job"},
    { value: 'C', text: "Class"},
    { value: 'B', text: "To Buy"},
    { value: 'S', text: "To Sell"},
    { value: 'O', text: "CBO"},
  ];
  selected_category = '';
  description = '';
  errors: string[] = [];

  async submit() {
    this.errors = [];
    if (!this.title) {
      this.errors.push("title cannot be empty");
    }
    if (!this.selected_category) {
      this.errors.push("category must be selected");
    }
    if (!this.description) {
      this.errors.push("description cannot be empty");
    }

    if (this.errors.length === 0) {
      const title = this.title;
      const category = this.selected_category;
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
