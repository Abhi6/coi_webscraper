import os
import json

allFiles = os.listdir("/Users/abhinavmara/Desktop/coi_webscraper/states")

allStates = []

for f in allFiles:
    with open (f"/Users/abhinavmara/Desktop/coi_webscraper/states/{f}", "r") as file:
        data = json.load(file)
        allStates.append(data)

with open("allStates.json", "w") as out:
    json.dump(allStates, out, indent=4)