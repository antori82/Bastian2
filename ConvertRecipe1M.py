import json

with open("Data/RECIPE1M/layer2.json", "r") as read_file:
    data = json.load(read_file)

with open("Data/RECIPE1M/layer2_pp.json", "w") as write_file:
    json.dump(data, write_file, indent=4, sort_keys=True)

