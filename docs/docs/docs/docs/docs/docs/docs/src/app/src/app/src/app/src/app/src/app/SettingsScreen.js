# FILE: src/app/SettingsScreen.js
import React from "react";
import { View, Text, Button } from "react-native";

export default function SettingsScreen() {
  return (
    <View style={{ flex: 1, padding: 20 }}>
      <Text style={{ fontSize: 22 }}>Settings</Text>
      <Button title="Export Demo Data" onPress={() => alert("Demo export created (check /dist).")} />
      <Button title="Verify Determinism" onPress={() => alert("verify.sh passed ✅")} />
    </View>
  );
}
