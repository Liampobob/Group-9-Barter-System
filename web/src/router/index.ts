import store from "@/store";
import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Home from "../views/Home.vue";
/*
 * Note: Lazy loading some routes generate a specific file for the routes which are lazy loaded.
 * This enables for loading a specific file instead of the whole bundle for some routes.
 */
const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/about",
    name: "About",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/login",
    name: "Login",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Login.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  if (
    to.matched.some((record) => record.meta.requiresAuth) &&
    !store.getters["userStore/isLoggedIn"]
  ) {
    // Make authentificated pages redirect to /Login if user is not logged in
    next({ name: "Login" });
    return;
  }
  next();
});

export default router;
