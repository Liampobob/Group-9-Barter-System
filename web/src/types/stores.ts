import {User} from './User';

export interface RootState {}

export interface SampleState {
  user: User;
}

export interface UserState {
  user: User;
  isLoggedIn: boolean;
}
