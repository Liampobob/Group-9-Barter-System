export interface User {
  facebook_id?: string;
  is_business?: boolean;
  location: {
    lattitude?: number;
    longitude?: number;
  }
  name: string;
  phone_number?: number;
  username: string;
  bio?: string;
}
