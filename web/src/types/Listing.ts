import { User } from "./User";

export interface Listing {
    title: string;
    category: string;
    description: string;
    posted_by: User;
  }
