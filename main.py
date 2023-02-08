import requests
import json

hero_list = ['Hulk', 'Captain America', 'Thanos']
name_hero_dict = {}
intelligence_list = {'Hulk': 0, 'Captain america': 0, 'Thanos': 0}

url = "https://akabab.github.io/superhero-api/api/all.json"
heroes = json.loads(requests.get(url).content)

for name_h in heroes:
    if name_h['name'] in hero_list:
        hero_key = name_h['name']
        hero_values = name_h['powerstats']['intelligence']
        name_hero_dict[hero_key] = int(hero_values)


def most_intelligent(list):
    return max(list)


print(f"Самый умный супер гирой: {most_intelligent(intelligence_list)}")
