import {User} from '@/types/User';
import {Module} from 'vuex';
import {RootState, SampleState} from '@/types/stores';

/*
 * Quick intro to stores & state. Components trigger actions which usually fetch / obtain some data.
 * Then a mutation is triggered which updates the values of the store.
 * The values in the store are imported by components such as to avoid component-level logic.
 */

export enum SampleActions {
  CHANGE_NAME = 'CHANGE_NAME'
}

const testModule: Module<SampleState, RootState> = {
  namespaced: true,
  state: {
    user: {name: ''}
  },
  mutations: {
    [SampleActions.CHANGE_NAME](state: SampleState, user: User) {
      state.user = user;
    }
  },
  actions: {
    changeName({commit, state}) {
      console.log(state.user.name);
      commit(SampleActions.CHANGE_NAME, {name: 'hello!'});
    }
  },
  getters: {
    user: state => state.user
  }
};

export default testModule;
