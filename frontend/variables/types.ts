export type User = {
    role: number;
    phone_number: string;
}

export type UserProfile = {
    user: User;
    name: string;
    major: string;
    grade: number;
    position: string;
    pitcher: boolean;
}