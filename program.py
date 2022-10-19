import json
import requests

response = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
populace = response.text
populace = json.loads(populace)
vystup = {}
for row in populace["data"]:
    vystup[row["Year"]] = row["Population"]
with open("population_usa.json", mode="w", encoding="utf-8") as soubor:
    json.dump(vystup, soubor, indent=4)