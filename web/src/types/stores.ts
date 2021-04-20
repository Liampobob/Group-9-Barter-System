import { User } from "./User";
import { Listing } from "./Listing";
import { Review } from "./Review";

export interface RootState { }

export interface SampleState {
  user: User | undefined;
}

export interface UserState {
  user?: User;
  token?: string;
  error: String;
  selectedUser?: User;
  selectedUserReviews?: Review[]
}

export interface ListingsState {
  listings: any[];
  featuredListing: Listing;
}