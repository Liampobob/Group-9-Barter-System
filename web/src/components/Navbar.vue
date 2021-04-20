<template>
    <nav class="navbar is-white" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
            <a class="navbar-item" @click="this.$router.push({name:'SEARCH'})">
                <img src="../imgs/logo.png" width="112" height="28">
            </a>
            <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample" @click="changeNavbar()">
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
            </a>
        </div>

        <div class="navbar-menu">
            <div class="navbar-start">
            <a class="navbar-item" @click="this.$router.push({name:'LISTINGS'})">
                Listings
            </a>
            <a class="navbar-item" @click="this.$router.push({name:'SEARCH'})">
                Search
            </a>
            <a class="navbar-item" @click="this.$router.push({name:'NEW_LISTING'})">
                Create Listing
            </a>
            <a class="navbar-item" @click="this.$router.push({name:'PROFILE'})">
                Profile
            </a>
            <a class="navbar-item" @click="this.$router.push({name:'SIGN_OUT'})">
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
import { ROUTE_NAMES } from "../router";

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
