import store from "@/store";
import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import Register from "../views/Register.vue";
import Search from "../views/Search.vue";
import Worker from "../views/Worker.vue";
import Profile from "../views/Profile.vue";
import Listings from "../views/Listings.vue";
import Listing from "../views/Listing.vue";
import NewListing from "../views/NewListing.vue";
import SignOut from "../views/SignOut.vue";

export enum ROUTE_NAMES {
  HOME = "HOME",
  LOGIN = "LOGIN",
  ABOUT = "ABOUT",
  SEARCH = "SEARCH",
  LISTINGS = "LISTINGS",
  LISTING = "LISTING",
  NEW_LISTING = "NEW_LISTING",
  PROFILE = "PROFILE",
  REGISTER = "REGISTER",
  WORKER = "WORKER",
  SIGN_OUT = "SIGN_OUT"
}

/*
 * Note: Lazy loading some routes generate a specific file for the routes which are lazy loaded.
 * This enables for loading a specific file instead of the whole bundle for some routes.
 */
const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: ROUTE_NAMES.HOME,
    component: Home,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/about",
    name: ROUTE_NAMES.ABOUT,
    component: About,
  },
  {
    path: "/login",
    name: ROUTE_NAMES.LOGIN,
    component: () =>
      import(/* webpackChunkName: "login" */ "../views/Login.vue"),
  },
  {
    path: "/register",
    name: ROUTE_NAMES.REGISTER,
    component: Register
  },
  {
    path: "/search",
    name: ROUTE_NAMES.SEARCH,
    component: Search
  },
  {
    path: "/newListing",
    name: ROUTE_NAMES.NEW_LISTING,
    component: NewListing
  },
  {
    path: "/listings",
    name: ROUTE_NAMES.LISTINGS,
    component: Listings
  },
  {
    path: "/listing/:title",
    name: ROUTE_NAMES.LISTING,
    component: Listing
  },
  {
    path: "/worker/:username",
    name: ROUTE_NAMES.WORKER,
    component: Worker
  },
  {
    path: "/profile",
    name: ROUTE_NAMES.PROFILE,
    component: Profile
  },
  {
    path: "/signout",
    name: ROUTE_NAMES.SIGN_OUT,
    component: SignOut
  }
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  if (
    to.matched.some((record) => record.meta.requiresAuth) &&
    !store.getters["userStore/isLoggedIn"]
  ) {
    // Make authentificated pages redirect to /Login if user is not logged in
    next({ name: ROUTE_NAMES.LOGIN });
    return;
  }
  next();
});

