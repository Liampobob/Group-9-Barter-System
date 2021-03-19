import { Module } from "vuex";
import { RootState, UserState } from "@/types/stores";
import { ROUTE_NAMES, router } from "@/router";
import axios from "@/shared/axios";
import { User } from "@/types/User";

export enum UserActions {
  LOGIN = "LOGIN",
  LOG_OUT = "LOG_OUT",
  ERROR_LOGIN = "ERROR_LOGIN",
}

const userStore: Module<UserState, RootState> = {
  namespaced: true,
  state: {
    user: undefined,
    error: "",
    token: localStorage.getItem('token') ?? undefined,
  },
  mutations: {
    [UserActions.LOGIN](state: UserState, payload: { user: User, token: string }) {
      localStorage.setItem('token', payload.token);
      state.user = payload.user;
      state.token = payload.token;
    },
    [UserActions.LOG_OUT](state: UserState) {
      state.user = undefined;
      state.token = undefined;
      localStorage.setItem('token', '');
    },
    [UserActions.ERROR_LOGIN](state: UserState, error: string) {
      state.error = error;
    },
  },
  actions: {
    logout({ commit }) {
      commit(UserActions.LOG_OUT);
    },
    async fbLogin({ commit }, payload: fb.AuthResponse) {
      const { data } = await axios.post('fb_auth', { accessToken: payload.accessToken });
      // TODO - get email from facebook if possible
      commit(UserActions.LOGIN, { user: data['user'], token: data['token'] });
      router.push({ name: ROUTE_NAMES.HOME });
    },
    errorLogin({ commit }) {
      commit(UserActions.ERROR_LOGIN, { error: "Facebook login failed!" });
    },
  },
  getters: {
    isLoggedIn: (state) => !!state.token,
    user: (state) => state.user,
    error: (state) => state.error,
    token: (state) => state.token ?? ''
  },
};

export default userStore;
