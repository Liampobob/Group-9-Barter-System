<template>
  <article class="container message is-dark">
    <div class="message-header">
      <p>Dark</p>
      <button class="delete" aria-label="delete"></button>
    </div>
    <div class="message-body">
      {{ msg }}
    </div>
  </article>
</template>

<script lang="ts">
import {Options, Vue} from 'vue-class-component';

@Options({
  props: {
    msg: String
  }
})
export default class HelloWorld extends Vue {
  msg!: string;
}
</script>

<!-- "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss"></style>
