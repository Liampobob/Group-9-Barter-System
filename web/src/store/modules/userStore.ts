import {Module} from 'vuex';
import {RootState, UserState} from '@/types/stores';

export enum UserActions {
  LOGIN = 'LOGIN',
  LOG_OUT = 'LOG_OUT'
}

const userStore: Module<UserState, RootState> = {
  namespaced: true,
  state: {
    user: {name: ''},
    isLoggedIn: false,
  },
  mutations: {
    [UserActions.LOGIN](state: UserState) {
      state.isLoggedIn = true;
    },
    [UserActions.LOG_OUT](state: UserState) {
      state.isLoggedIn = false;
    }
  },
  actions: {
    logout({commit}) {
      commit(UserActions.LOG_OUT);
    },
    login({commit}) {
      commit(UserActions.LOGIN, {name: 'hello!'});
    }
  },
  getters: {
    isLoggedIn: state => state.isLoggedIn
  }
};

export default userStore;
