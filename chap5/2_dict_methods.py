marks = {
    "Ritika": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Ritika"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Ritika": 99, "Renuka": 100})
# print(marks)

print(marks.get("Ritika2")) # Prints None
print(marks["Ritika2"]) # Returns an error