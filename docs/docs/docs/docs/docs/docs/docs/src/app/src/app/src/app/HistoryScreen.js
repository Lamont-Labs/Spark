# FILE: src/app/HistoryScreen.js
import React, { useEffect, useState } from "react";
import { View, Text, FlatList } from "react-native";
import { getEntries } from "../core/streak_engine";

export default function HistoryScreen() {
  const [entries, setEntries] = useState([]);

  useEffect(() => {
    getEntries().then(setEntries);
  }, []);

  return (
    <View style={{ flex: 1, padding: 20 }}>
      <Text style={{ fontSize: 22, marginBottom: 10 }}>History</Text>
      <FlatList
        data={entries}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <View style={{ marginBottom: 10 }}>
            <Text>Gratitude: {item.gratitude}</Text>
            <Text>Win: {item.win}</Text>
            <Text>Affirmation: {item.affirmation}</Text>
          </View>
        )}
      />
    </View>
  );
}
