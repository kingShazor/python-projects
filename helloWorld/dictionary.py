students = {
    "100023": "2.0",
    "103501": "2.3",
    "100320": "4.0"
}

name = input("Gib die Matrikelnummer eines Sutdenten ein:")
if name in students:
    print(f"mrn.: {name} hat die Note: {students[name]}")
else:
    print(f"mrn.: {name} ist nicht im Verzeichnis") 
