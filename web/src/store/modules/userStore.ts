import { Module } from "vuex";
import { RootState, UserState } from "@/types/stores";
import { ROUTE_NAMES, router } from "@/router";
import axios from "@/shared/axios";
import { User } from "@/types/User";

export enum UserActions {
  LOGIN = "LOGIN",
  LOG_OUT = "LOG_OUT",
  ERROR_LOGIN = "ERROR_LOGIN",
  LOAD_USER = "LOAD_USER"
}

const userStore: Module<UserState, RootState> = {
  namespaced: true,
  state: {
    user: undefined,
    error: "",
    token: localStorage.getItem('token') ?? undefined,
    selectedUser: undefined
  },
  mutations: {
    [UserActions.LOGIN](state: UserState, payload: { user: User; token: string }) {
      localStorage.setItem('token', payload.token);
      state.user = payload.user;
      state.token = payload.token;
    },
    [UserActions.LOG_OUT](state: UserState) {
      state.user = undefined;
      state.token = undefined;
      state.error = "";
      localStorage.setItem('token', '');
    },
    [UserActions.ERROR_LOGIN](state: UserState, error: string) {
      state.error = error;
    },
    [UserActions.LOAD_USER](state: UserState, payload: User) {
      state.selectedUser = payload;
    },
  },
  actions: {
    logout({ commit }) {
      commit(UserActions.LOG_OUT);
      router.push({ name: ROUTE_NAMES.LOGIN });
    },
    async fbLogin({ commit }, payload: fb.AuthResponse) {
      const { data } = await axios.post('fb_auth', { accessToken: payload.accessToken });
      // TODO - get email from facebook if possible
      commit(UserActions.LOGIN, { user: data['user'], token: data['token'] });
      router.push({ name: ROUTE_NAMES.HOME });
    },
    async auth({ commit }, payload: { username: string; password: string }) {
      try {
        const { data } = await axios.post('auth', payload);
        commit(UserActions.LOGIN, { user: data['user'], token: data['token'] });
        router.push({ name: ROUTE_NAMES.HOME });
      } catch (err) {
        commit(UserActions.ERROR_LOGIN, { error: 'No user match the provided credentials' });
      }
    },
    errorLogin({ commit }) {
      commit(UserActions.ERROR_LOGIN, { error: "Facebook login failed!" });
    },
    async register({ commit }, payload: { username: string; password: string; phone_number: string; bio: string; name: string }) {
      try {
        const { data } = await axios.post('register', payload);
        commit(UserActions.LOGIN, { user: data['user'], token: data['token'] });
        router.push({ name: ROUTE_NAMES.HOME });
        return null;
      } catch (err) {
        commit(UserActions.ERROR_LOGIN, { error: 'No user match the provided credentials' });
        return { errors: err.message }
      }
    },
    async getWorker({ commit }, payload: { username: string }) {
      try {
        const { data } = await axios.get(`worker?username=${payload.username}`);
        commit(UserActions.LOAD_USER, data['user']);
      } catch (err) {
        return {error: 'An error occured.'}
      }
    }
  },
  getters: {
    isLoggedIn: (state) => !!state.token,
    user: (state) => state.user,
    error: (state) => state.error,
    token: (state) => state.token ?? '',
    selectedUser: (state) => state.selectedUser
  },
};

export default userStore;
