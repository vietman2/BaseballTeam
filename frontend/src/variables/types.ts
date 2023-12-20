import { UserType, Position } from './enums';

type UserTypeKey = keyof typeof UserType;
type PositionKey = keyof typeof Position;

export type User = {
  id: number;
  user_type: UserTypeKey;
  name: string;
  phone_number: string;
  freshman_year: number;
  major: string;
  grade: number;
  position: PositionKey;
};

export type DailyParticipation = {
  participation: boolean;
  start_time?: string;
  end_time?: string;
  reason?: string;
};

export type WeeklyParticipation = {
  no: number;
  name: string;
  major: string;
  grade: number;
  phone_number: string;
  monday: DailyParticipation;
  tuesday: DailyParticipation;
  wednesday: DailyParticipation;
  thursday: DailyParticipation;
  friday: DailyParticipation;
  saturday: DailyParticipation;
  sunday: DailyParticipation;
  total: number;
};
