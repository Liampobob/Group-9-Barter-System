import { Module } from "vuex";
import { RootState, ListingsState } from "@/types/stores";
import { Listing } from "@/types/Listing";
import { ROUTE_NAMES, router } from "@/router";
import axios from "@/shared/axios";

const listingsStore: Module<ListingsState, RootState> = {
  namespaced: true,
  state: {
    listings: [],
  },
  mutations: {
    ["Set"](state: ListingsState, newListings: Listing[]) {
      state.listings = newListings; 
    },
  },
  actions: {
    setListings({ commit }, newListings: Listing[]) {
        commit("Set", newListings);
        router.push({ name: ROUTE_NAMES.LISTINGS });
    },
    async searchListings({ commit }, searchInfo: {terms: string; category: string}) {
      const { data } = await axios.post('search', searchInfo);
      commit("Set", data['data'].map((a: {title: string; category: string; description: string; owner: string}) => { return {title: a.title, category: a.category, description: a.description, owner: a.owner};}));
      console.log(data);
      router.push({ name: ROUTE_NAMES.LISTINGS });
    },
    async createListing({ }, searchInfo: {terms: string; category: string; description: string; username: string}) {
      const { data } = await axios.post('createListing', searchInfo);
      router.push({ name: ROUTE_NAMES.NEW_LISTING });
    },
  },
  getters: {
    getListings: (state) => state.listings,
  },
};

export default listingsStore;
