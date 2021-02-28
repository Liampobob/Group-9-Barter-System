import { User } from "./User";

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
