import { User } from "./User";
import { Listing } from "./Listing";

export interface RootState {}

export interface SampleState {
  user: User;
}

export interface UserState {
  user: User;
  auth: fb.AuthResponse | undefined;
  isLoggedIn: boolean;
  error: String;
}

export interface ListingsState{
  listings: Listing[];
}