<template>
  <div>
    <button class="button is-primary" v-on:click="changeName()">Test</button>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { mapActions } from "vuex";

@Options({
  components: {},
  computed: {},
})
export default class Profile extends Vue {
  username = "";

  mounted() {
    this.username = this.$route.params["username"] ?? "";
    if(this.username) {
        
    }
  }
}
</script>
