import { User } from "./User";

export interface RootState { }

export interface SampleState {
  user: User | undefined;
}

export interface UserState {
  user?: User;
  token?: string;
  error: String;
}
