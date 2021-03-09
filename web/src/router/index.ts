import store from "@/store";
import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Home from "../views/Home.vue";

export enum ROUTE_NAMES {
  HOME = "HOME",
  LOGIN = "LOGIN",
  ABOUT = "ABOUT",
  SEARCH = "SEARCH",
  LISTINGS = "LISTINGS",
  PROFILE = "PROFILE",
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
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/login",
    name: ROUTE_NAMES.LOGIN,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Login.vue"),
  },
  {
    path: "/search",
    name: ROUTE_NAMES.SEARCH,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Search.vue"),
  },
  {
    path: "/listings",
    name: ROUTE_NAMES.LISTINGS,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Listings.vue"),
  },
  {
    path: "/profile",
    name: ROUTE_NAMES.PROFILE,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Profile.vue"),
  },
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
