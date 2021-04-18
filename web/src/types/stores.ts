import { User } from "./User";
import { Listing } from "./Listing";

export interface RootState { }

export interface SampleState {
  user: User | undefined;
}

export interface UserState {
  user?: User;
  token?: string;
  error: String;
  selectedUser?: User;
}

export interface ListingsState {
  listings: Listing[];
  featuredListing: Listing;
}