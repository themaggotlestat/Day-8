computer = {
    "brand": "HP",
    "model": "Omen",
    "ram": 16,
    "storage": 238
}

for item in computer:
    print(f"{item}: {computer[item]}")
    if item == "ram":
        if computer[item] >= 16:
            print("Enough RAM")
        else:
            print("Not Enough RAM")
    if item == "storage":
        if computer[item] >= 256:
            print("Enough storage")
        else:
            print("Not Enough storage")