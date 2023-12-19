const UserType = {
    NEW_ACCOUNT: { value: 0, label: "신규계정"},
    ADMIN: { value: 1, label: "관리자"},
    CAPTAIN: { value: 2, label: "주장"},
    VICE_CAPTAIN: { value: 3, label: "부주장"},
    MANAGER: { value: 4, label: "매니저"},
    MEMBER: { value: 5, label: "부원"},
    MILITARY: { value: 6, label: "군입대중"},
    INACTIVE: { value: 7, label: "비활동부원"},
    DELETED: { value: 8, label: "탈퇴한 회원"},
}

const Position = {
    NEW: { value: 0, label: "신입"},
    PITCHER: { value: 1, label: "투수"},
    CATCHER: { value: 2, label: "포수"},
    FIRST_BASE: { value: 3, label: "1루수"},
    SECOND_BASE: { value: 4, label: "2루수"},
    THIRD_BASE: { value: 5, label: "3루수"},
    SHORTSTOP: { value: 6, label: "유격수"},
    LEFT_FIELD: { value: 7, label: "좌익수"},
    CENTER_FIELD: { value: 8, label: "중견수"},
    RIGHT_FIELD: { value: 9, label: "우익수"},
    MANAGER: { value: 10, label: "매니저"},
}

export { UserType, Position };
