import { Module } from "vuex";
import { RootState, UserState } from "@/types/stores";
import { ROUTE_NAMES, router } from "@/router";

export enum UserActions {
  LOGIN = "LOGIN",
  LOG_OUT = "LOG_OUT",
  ERROR_LOGIN = "ERROR_LOGIN",
}

const userStore: Module<UserState, RootState> = {
  namespaced: true,
  state: {
    user: { name: "" },
    isLoggedIn: false, // TODO load JWT from local storage
    error: "",
    auth: undefined,
  },
  mutations: {
    [UserActions.LOGIN](state: UserState, payload: fb.AuthResponse) {
      console.log(payload);
      state.isLoggedIn = true;
      state.auth = payload; // TODO : pass tokens to server
    },
    [UserActions.LOG_OUT](state: UserState) {
      state.isLoggedIn = false;
      state.auth = undefined;
    },
    [UserActions.ERROR_LOGIN](state: UserState, error: string) {
      state.error = error;
    },
  },
  actions: {
    logout({ commit }) {
      commit(UserActions.LOG_OUT);
    },
    login({ commit }, payload: fb.AuthResponse) {
      commit(UserActions.LOGIN, payload);
      router.push({ name: ROUTE_NAMES.HOME });
    },
    errorLogin({ commit }) {
      commit(UserActions.ERROR_LOGIN, { error: "Facebook login failed!" });
    },
  },
  getters: {
    isLoggedIn: (state) => state.isLoggedIn,
    error: (state) => state.error,
  },
};

export default userStore;
