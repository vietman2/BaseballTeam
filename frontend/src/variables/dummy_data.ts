import { User } from "./types";

const users: User[] = [
  {
    id: 1,
    user_type: "CAPTAIN",
    name: "주우장",
    phone_number: "010-1234-5678",
    freshman_year: 2018,
    major: "컴퓨터공학과",
    grade: 3,
    position: "CENTER_FIELD",
  },
  {
    id: 2,
    user_type: "VICE_CAPTAIN",
    name: "부주장",
    phone_number: "010-1234-4321",
    freshman_year: 2022,
    major: "컴퓨터공학과",
    grade: 2,
    position: "LEFT_FIELD",
  },
  {
    id: 3,
    user_type: "MEMBER",
    name: "평부원",
    phone_number: "010-1234-1234",
    freshman_year: 2023,
    major: "컴퓨터공학과",
    grade: 1,
    position: "CATCHER",
  },
];

const weeklyParticipations = [
  {
    no: 1,
    name: "주우장",
    major: "컴퓨터공학과",
    grade: 3,
    phone_number: "010-1234-5678",
    monday: {
      participation: true,
      start_time: "17:00",
      end_time: "21:00",
    },
    tuesday: {
      participation: true,
      start_time: "10:00",
      end_time: "12:00",
    },
    wednesday: {
      participation: false,
      reason: "과외",
    },
    thursday: {
      participation: true,
      start_time: "17:00",
      end_time: "21:00",
    },
    friday: {
      participation: false,
      reason: "수업",
    },
    saturday: {
      participation: true,
      start_time: "08:30",
      end_time: "13:00",
    },
    sunday: {
      participation: false,
      reason: "훈련없음",
    },
    total: 4,
  },
  {
    no: 2,
    name: "부주장",
    major: "경영학과",
    grade: 2,
    phone_number: "010-1234-4321",
    monday: {
      participation: true,
      start_time: "17:00",
      end_time: "21:00",
    },
    tuesday: {
      participation: true,
      start_time: "17:00",
      end_time: "19:00",
    },
    wednesday: {
      participation: true,
      start_time: "17:30",
      end_time: "20:30",
    },
    thursday: {
      participation: true,
      start_time: "18:30",
      end_time: "21:00",
    },
    friday: {
      participation: false,
      reason: "봉사",
    },
    saturday: {
      participation: true,
      start_time: "08:30",
      end_time: "13:00",
    },
    sunday: {
      participation: false,
      reason: "훈련없음",
    },
    total: 5,
  },
  {
    no: 3,
    name: "평부원",
    major: "체육교육과",
    grade: 1,
    phone_number: "010-1234-1234",
    monday: {
      participation: true,
      start_time: "16:30",
      end_time: "19:30",
    },
    tuesday: {
      participation: true,
      start_time: "16:00",
      end_time: "20:00",
    },
    wednesday: {
      participation: false,
      reason: "시험",
    },
    thursday: {
      participation: true,
      start_time: "19:30",
      end_time: "21:00",
    },
    friday: {
      participation: false,
      reason: "가족행사",
    },
    saturday: {
      participation: false,
      reason: "보강수업",
    },
    sunday: {
      participation: false,
      reason: "훈련없음",
    },
    total: 3,
  },
];

export { users, weeklyParticipations };
