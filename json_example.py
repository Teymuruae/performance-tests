import  json

json_str = """
{
  "name": "Иван",
  "age": 33,
  "address": {
    "country": "Russia",
    "city": "Moscow"
  }
}
"""

json_dict = json.loads(json_str)

json_string = json.dumps(json_dict, ensure_ascii=False, indent=2)

with open('user.json', encoding='utf-8') as file:
    json_from_file = json.load(file)

with open('user2.json', 'w', encoding='utf-8') as file:
    json.dump(json_from_file, file, ensure_ascii=False, indent=2)