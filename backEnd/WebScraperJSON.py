import requests
inputUrl = input("Type the Url of any shopify website here")
url = inputUrl + '.json'
resp = requests.get(url)
data = resp.json()["product"]

# getting the name
def itemName():
    return data["title"]

# getting the options like size
def itemOptions():
    options = []
    for item in (data["variants"]):
        if item["option1"] not in options:
            options.append(item["option1"])
    return options

# calling and printing
print("Name:" + itemName())
print("Available sizes: ", end='')
for itemOption in itemOptions():
    print(itemOption + ", ", end='')
