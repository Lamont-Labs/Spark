# FILE: src/app/TodayScreen.js
import React, { useState } from "react";
import { View, Text, TextInput, Button, StyleSheet } from "react-native";
import { saveEntry } from "../core/streak_engine";

export default function TodayScreen() {
  const [gratitude, setGratitude] = useState("");
  const [win, setWin] = useState("");
  const [affirmation, setAffirmation] = useState("");
  const [status, setStatus] = useState("");

  const handleSave = async () => {
    await saveEntry({ gratitude, win, affirmation });
    setStatus("Saved locally ✅");
    setGratitude("");
    setWin("");
    setAffirmation("");
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Today's Reflections</Text>
      <TextInput style={styles.input} placeholder="Gratitude" value={gratitude} onChangeText={setGratitude}/>
      <TextInput style={styles.input} placeholder="Win" value={win} onChangeText={setWin}/>
      <TextInput style={styles.input} placeholder="Affirmation" value={affirmation} onChangeText={setAffirmation}/>
      <Button title="Save Entry" onPress={handleSave}/>
      <Text style={styles.status}>{status}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, backgroundColor: "#fff" },
  header: { fontSize: 22, fontWeight: "600", marginBottom: 12 },
  input: { borderWidth: 1, borderColor: "#ccc", borderRadius: 6, marginVertical: 5, padding: 10 },
  status: { marginTop: 10, color: "green" },
});
