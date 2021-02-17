import {createStore} from 'vuex';
import testModule from './modules/testModule';

// Root store, composed of sub-stores with specific use cases.
export default createStore({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    testModule
  }
});
