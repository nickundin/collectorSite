import requests
inputUrl = input("Type the Url of any shopify website here")
url = inputUrl + '.json'
resp = requests.get(url)
data = resp.json()["product"]

# getting the name
def itemName():
    return data["title"]


options = []
for item in (data["variants"]):
    if item["option1"] not in options:
        options.append(item["option1"])
print(options)
