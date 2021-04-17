import { Module } from "vuex";
import { RootState, ListingsState } from "@/types/stores";
import { Listing } from "@/types/Listing";
import { ROUTE_NAMES, router } from "@/router";
import axios from "@/shared/axios";

const listingsStore: Module<ListingsState, RootState> = {
  namespaced: true,
  state: {
    listings: [],
    featuredListing: {title: '', category:'', description: '', owner: ''},
  },
  mutations: {
    ["SetListings"](state: ListingsState, newListings: Listing[]) {
      state.listings = newListings; 
    },
    ["SetFeaturedListing"](state: ListingsState, newListing: Listing) {
      state.featuredListing = newListing; 
    },
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
    async createListing({ commit }, payload: {
        title:string;
        category:string;
        description:string
    }) {
      try {
        const { data } = await axios.post('', payload);
        //commit(, {})
        //
      } catch (err) {
        return { errors: err.message}
      }

    },
    async searchListings({ commit }, searchInfo: {terms: string; category: string}) {
      const { data } = await axios.post('search', searchInfo);
      commit("SetListings", data['listings'].map((a: {title: string; category: string; description: string; owner: string}) => { return {title: a.title, category: a.category, description: a.description, owner: a.owner};}));
      commit("SetFeaturedListing", {title: data['featured'].title, category: data['featured'].category, description: data['featured'].description, owner: data['featured'].owner});
      console.log(data);
      router.push({ name: ROUTE_NAMES.LISTINGS });
    },
    async createListing({ commit }, searchInfo: {terms: string; category: string; description: string; username: string}) {
      const { data } = await axios.post('createListing', searchInfo);
      router.push({ name: ROUTE_NAMES.NEW_LISTING });
    },
  },
  getters: {
    getListings: (state) => state.listings,
    getFeaturedListing: (state) => state.featuredListing,
  },
};

export default listingsStore;
