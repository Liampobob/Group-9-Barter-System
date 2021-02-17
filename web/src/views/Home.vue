<template>
  <div>
    <HelloWorld v-bind:msg="getUser.name" />
    <button class="button is-primary" v-on:click="changeName()">Execute a store action</button>
  </div>
</template>

<script lang="ts">
import HelloWorld from '@/components/HelloWorld.vue';
import {Options, Vue} from 'vue-class-component';
import {mapActions} from 'vuex';

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
    ...mapActions('testModule', ['changeName'])
  }
})
export default class Home extends Vue {}
</script>
