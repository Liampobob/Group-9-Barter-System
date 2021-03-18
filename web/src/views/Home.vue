<template>
  <div>
    <HelloWorld v-bind:msg="getUser.name" />
    <button class="button is-primary" v-on:click="changeName()">Execute a store action</button>
    <button class="button is-primary" v-on:click="call()">Call backend</button>
  </div>
</template>

<script lang="ts">
import HelloWorld from '@/components/HelloWorld.vue';
import {Options, Vue} from 'vue-class-component';
import {mapActions} from 'vuex';
import axios from "@/shared/axios";

@Options({
  components: {
    HelloWorld
  },
  computed: {
    getUser() {
      return this.$store.state.testModule.user;
    }
  },
  methods: {
    // Get action changeName from testModule store
    ...mapActions('testModule', ['changeName']),
    call: async () => {
      const a = await axios.get('status');
      console.log(a);
    }
  }
})
export default class Home extends Vue {}
</script>
