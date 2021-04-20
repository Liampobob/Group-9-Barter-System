<template>
  <div>
    <navbar/>
    <section class="hero is-primary is-fullheight-with-navbar">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-5-tablet is-4-desktop is-3-widescreen">
            <div class="box has-text-centered">
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import Navbar from "../components/Navbar.vue";

@Options({
  components: {
    Navbar
  },
  computed: {
  },
  methods: {
  },
})
export default class Home extends Vue {
  mounted() {
    this.$store.dispatch("userStore/logout");
  }
}
</script>
