<template>
    <nav class="navbar is-white" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
            <a class="navbar-item" href="/login">
            <img src="../imgs/logo.png" width="112" height="28">
            </a>
            <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample" @click="changeNavbar()">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            </a>
        </div>

        <div id="navbarBasicExample" class="navbar-menu">
            <div class="navbar-start">
            <a class="navbar-item" href="/search">
                Search
            </a>
            <a class="navbar-item" href="/newlisting">
                Create Listing
            </a>
            <a class="navbar-item" href="/profile">
                Profile
            </a>
            <a class="navbar-item" href="/signout">
                Log Out
            </a>
            </div>
        </div>
    </nav>
</template>

<script lang="ts">
// Typescript behaves weirdly with the Facebook JS SDK
/* eslint-disable */

import { Options, Vue } from "vue-class-component";

@Options({
  components: {},
  computed: {},
})
export default class Navbar extends Vue {
  changeNavbar() {
    const menu = document.querySelector(".navbar-menu");
    if (menu != null) menu.classList.toggle("is-active");
    const burger = document.querySelector(".navbar-burger");
    if (burger != null) burger.classList.toggle("is-active");
  }

}
</script>
