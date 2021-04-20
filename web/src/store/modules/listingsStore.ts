import { Module } from "vuex";
import { RootState, ListingsState } from "@/types/stores";
import { Listing } from "@/types/Listing";
import { ROUTE_NAMES, router } from "@/router";
import axios from "@/shared/axios";

const listingsStore: Module<ListingsState, RootState> = {
  namespaced: true,
  state: {
    listings: [],
    featuredListing: { title: '', category: '', description: '', posted_by: {location: { lattitude: 0, longitude: 0 }, name: "", username: ""} },
  },
  mutations: {
    ["SetListings"](state: ListingsState, newListings: Listing[]) {
      state.listings = newListings;
    },
    ["SetFeaturedListing"](state: ListingsState, newListing: Listing) {
      state.featuredListing = newListing;
    },
    ["AddListing"](state: ListingsState, newListing: Listing) {
      state.listings.push(newListing);
    }
  },
  actions: {
    setListings({ commit }, newListings: Listing[]) {
      commit("SetListings", newListings);
      router.push({ name: ROUTE_NAMES.LISTINGS });
    },
    setFeaturedListing({ commit }, newListing: Listing) {
      commit("SetFeaturedListing", newListing);
      router.push({ name: ROUTE_NAMES.LISTINGS });
    },
    async searchListings({ commit }, searchInfo: { terms: string; category: string }) {
      const { data } = await axios.post('search', searchInfo);
      commit("SetListings", data['listings']);
      commit("SetFeaturedListing", { ...data['featured'] });
      router.push({ name: ROUTE_NAMES.LISTINGS });
    },
    async createListing({ commit }, searchInfo: { title: string; category: string; description: string; }) {
      const { data } = await axios.post('createListing', searchInfo);
      commit("AddListing", data['listing'])
      router.push({ name: ROUTE_NAMES.LISTING, params: { title: data['listing']['title'] ?? '' } });
    },
  },
  getters: {
    getListings: (state) => state.listings,
    getFeaturedListing: (state) => state.featuredListing,
  },
};

export default listingsStore;
