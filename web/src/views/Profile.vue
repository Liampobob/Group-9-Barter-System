<template>
  <div>
    <h1>{{theError}}</h1>
  </div>
</template>

<script lang="ts">
import {Options, Vue} from 'vue-class-component';
import store from "@/store";

@Options({
  components: {
  },
  computed: {
  },
})
export default class Profile extends Vue {
  error = '';
  get theError() {return this.error;}

  async mounted() {
      const resp = store.getters["userStore/user"];
      console.log(resp);

      if (resp?.["error"]) {
      this.error = resp["error"];
      }
  }
  
}
</script>
