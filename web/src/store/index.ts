import { createStore } from 'vuex';
import testModule from './modules/testModule';
import userStore from './modules/userStore';
import listingsStore from './modules/listingsStore';

// Root store, composed of sub-stores with specific use cases.
export default createStore({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    testModule,
    userStore,
    listingsStore,
  }
});
