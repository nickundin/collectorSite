from bs4 import BeautifulSoup
import requests
import urllib

# using a keyboard website as an example,
url = 'https://kbdfans.com/products/ic-baguette-mechanical-keyboard'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'lxml')



# find price
def priceFind():
    price = soup.find('span', class_='theme-money large-title')
    return price.text


# find name
def nameFind():
    name = soup.find('h1', class_='product-detail__title small-title')
    return name.text


# find colors
def colorFind():
    colors = soup.find('div', class_='selector-wrapper styled-dropdown styled-dropdown--label-small row js')
    returnString = ""
    for colorOption in colors.find_all('option'):
        returnString += ' ' + colorOption.text + ','
    return returnString


# executing stuff
price = priceFind()
name = nameFind()
colors = colorFind()

print(f"The {name} costs {price} dollars and comes in {colors}")

