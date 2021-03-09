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
      state.listings = newListings; // TODO : pass tokens to server
    },
  },
  actions: {
    setListings({ commit }, newListings: Listing[]) {
        commit("Set", newListings);
        router.push({ name: ROUTE_NAMES.LISTINGS });
    },
  },
  getters: {
    getListings: (state) => state.listings,
  },
};

export default listingsStore;
