import json
import requests
r = requests.get('http://localhost:3000')
data=r.json()
output = ""
i = 0

for item in data:
    for att, value in item.items():
        if att == "name":
            tempName = value.capitalize()
            output += tempName + " is "
        else:
            output += value + '\n'

print(output)