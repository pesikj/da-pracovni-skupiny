import json

with open("zavod.json", encoding="utf-8") as soubor:
    zavod = json.load(soubor)

print(zavod[0])