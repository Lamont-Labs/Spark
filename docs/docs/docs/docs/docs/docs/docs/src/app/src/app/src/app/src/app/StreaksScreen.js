# FILE: src/app/StreaksScreen.js
import React, { useEffect, useState } from "react";
import { View, Text } from "react-native";
import { getStreakStatus } from "../core/streak_engine";

export default function StreaksScreen() {
  const [status, setStatus] = useState(null);

  useEffect(() => {
    getStreakStatus().then(setStatus);
  }, []);

  if (!status) return <Text>Loading streak...</Text>;

  return (
    <View style={{ flex: 1, padding: 20 }}>
      <Text style={{ fontSize: 22 }}>Your Streak</Text>
      <Text>Current: {status.current} days</Text>
      <Text>Best: {status.best} days</Text>
      <Text>{status.message}</Text>
    </View>
  );
}
