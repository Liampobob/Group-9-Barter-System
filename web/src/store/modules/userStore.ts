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
  },
  mutations: {
    [UserActions.LOGIN](state: UserState, payload: User) {
      state.user = payload;
    },
    [UserActions.LOG_OUT](state: UserState) {
      state.user = undefined;
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
      const resp = await axios.post('auth', {accessToken: payload.accessToken});
      console.log(resp.data['user']);
        // TODO - get email from facebook
        commit(UserActions.LOGIN, resp.data['user']);
        router.push({ name: ROUTE_NAMES.HOME });
    },
    errorLogin({ commit }) {
      commit(UserActions.ERROR_LOGIN, { error: "Facebook login failed!" });
    },
  },
  getters: {
    isLoggedIn: (state) => !!state.user,
    user: (state) => state.user,
    error: (state) => state.error,
  },
};

export default userStore;
