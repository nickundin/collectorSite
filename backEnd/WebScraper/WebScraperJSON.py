import requests


# get the name of the item
def item_name(input_url):
    url = input_url + '.json'
    resp = requests.get(url)
    return resp.json()["product"]["title"]


# getting the options like size
def item_options(input_url):
    url = input_url + '.json'
    resp = requests.get(url)
    return resp.json()["product"]["variants"][0]["option1"]



