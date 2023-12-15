import json
file = open("ski_resort_info.json", "r")
jsonFile = json.load(file)
print(jsonFile)

