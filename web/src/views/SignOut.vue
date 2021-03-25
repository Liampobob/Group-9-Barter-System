<template>
  <section class="hero is-primary is-fullheight">
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
</template>

<script lang="ts">
import HelloWorld from "@/components/HelloWorld.vue";
import { Options, Vue } from "vue-class-component";
import { mapActions } from "vuex";
import axios from "@/shared/axios";

@Options({
  components: {
    HelloWorld,
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
