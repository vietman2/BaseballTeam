import { DataTable } from "react-native-paper";

import { weeklyParticipations } from "../../variables/dummy_data";
import { DailyParticipation } from "../../variables/types";

export default function WeeklyTable() {
    const getData = (day: DailyParticipation) => {
        if (day.participation === false) {
            return day.reason?.toString() ?? "X"
        }
        else return "O"
    }

    return (
        <DataTable>
            <DataTable.Header>
                <DataTable.Title numeric>No</DataTable.Title>
                <DataTable.Title>이름</DataTable.Title>
                <DataTable.Title>학과</DataTable.Title>
                <DataTable.Title numeric>학년</DataTable.Title>
                <DataTable.Title>연락처</DataTable.Title>
                <DataTable.Title>월</DataTable.Title>
                <DataTable.Title>화</DataTable.Title>
                <DataTable.Title>수</DataTable.Title>
                <DataTable.Title>목</DataTable.Title>
                <DataTable.Title>금</DataTable.Title>
                <DataTable.Title>토</DataTable.Title>
                <DataTable.Title>일</DataTable.Title>
                <DataTable.Title numeric>합</DataTable.Title>
            </DataTable.Header>

            {weeklyParticipations.map((participation, index) => (
                <DataTable.Row key={index}>
                    <DataTable.Cell numeric>{index + 1}</DataTable.Cell>
                    <DataTable.Cell>{participation.name}</DataTable.Cell>
                    <DataTable.Cell>{participation.major}</DataTable.Cell>
                    <DataTable.Cell numeric>{participation.grade}</DataTable.Cell>
                    <DataTable.Cell>{participation.phone_number}</DataTable.Cell>
                    <DataTable.Cell>{getData(participation.monday)}</DataTable.Cell>
                    <DataTable.Cell>{getData(participation.tuesday)}</DataTable.Cell>
                    <DataTable.Cell>{getData(participation.wednesday)}</DataTable.Cell>
                    <DataTable.Cell>{getData(participation.thursday)}</DataTable.Cell>
                    <DataTable.Cell>{getData(participation.friday)}</DataTable.Cell>
                    <DataTable.Cell>{getData(participation.saturday)}</DataTable.Cell>
                    <DataTable.Cell>{getData(participation.sunday)}</DataTable.Cell>
                    <DataTable.Cell>{participation.total}</DataTable.Cell>
                </DataTable.Row>
            ))}
        </DataTable>
    )
}
