import React from "react";
import { View, Text, TouchableOpacity, StyleSheet } from "react-native";
import { BottomTabScreenProps } from "@react-navigation/bottom-tabs"; // 사용 중인 네비게이션 라이브러리에 맞게 수정

type SettingsScreenProps = BottomTabScreenProps<any>; // BottomTabScreenProps에는 타입 매개변수로 'ParamList' 타입을 넣어주어야 할 수도 있습니다.

function SettingsScreen({ navigation }: SettingsScreenProps) {
    return (
        <View style={styles.container}>
            <TouchableOpacity onPress={() => navigation.navigate('Home')}>
                <Text style={styles.text}>SettingsScreen</Text>
            </TouchableOpacity>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: "center",
        justifyContent: "center",
    },
    text: {
        fontSize: 26,
        fontWeight: "bold",
    },
});

export default SettingsScreen;
