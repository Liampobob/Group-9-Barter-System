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
  contact_name?: string;
  description?: string;
  end_time?: number;
  start_time?: number;
  is_cbo?: boolean;
  work_tags?: string;
  working_days?: string
}
