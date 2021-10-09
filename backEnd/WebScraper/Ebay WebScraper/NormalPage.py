from bs4 import BeautifulSoup
import requests
import time


# take in product page link, return beautifulsoup object
def turn_to_soup(input_url):
    time.sleep(1)
    html = requests.get(input_url)
    return BeautifulSoup(html.text, 'lxml')


# get the name of the item
def item_name(input_url):
    soup = turn_to_soup(input_url)
    try:
        return soup.find("h1", class_="it-ttl").contents[1]
    except AttributeError:
        return soup.find("h1", class_="product-title").text


# getting the image
def item_image(input_url):
    soup = turn_to_soup(input_url)
    try:
        return soup.find("img", class_="img img300")["src"]
    except TypeError:
        return soup.find("a", class_="vi-image-gallery__enlarge-link").find("img")["data-src"]


# getting the price
def item_price(input_url):
    return turn_to_soup(input_url).find("span", class_="notranslate")["content"]


# getting the condition
def item_condition(input_url):
    soup = turn_to_soup(input_url)
    return soup.find("div", class_="u-flL condText").text


def item_seller(input_url):
    # return turn_to_soup(input_url).prettify
    try:
        return turn_to_soup(input_url).find("span", class_="mbg-nw").text
    except AttributeError:
        return turn_to_soup(input_url).findAll("span", class_="no-wrap")[1].find("a")["title"]


def item_availability(input_url):
    soup = turn_to_soup(input_url)
    soup1 = soup.find("span", class_="qtyTxt vi-bboxrev-dsplblk vi-qty-fixAlignment feedbackON")
    if soup1 is None:
        soup2 = soup.find("span", class_="qtyTxt vi-bboxrev-dsplblk vi-qty-fixAlignment feedbackON vi-vpqp-feedback")
        if soup2 is None:
            return "N/A"
        else:
            return soup2.find("span", class_="").text.strip()
    else:
        return soup1.find("span", class_="").text.strip()


def item_return_policy(input_url):
    soup = turn_to_soup(input_url)
    try:
        return soup.find("td", class_="rpWrapCol").find("span").find("span").text
    except AttributeError:
        return soup.find("td", class_="rpWrapCol").find("span").text


def item_attributes(input_url):
    product = {"item_name": item_name(input_url), "item_image": item_image(input_url),
               "item_price": item_price(input_url), "item_condition": item_condition(input_url),
               "item_seller": item_seller(input_url), "item_availability": item_availability(input_url),
               "item_return_policy": item_return_policy(input_url)}
    return product

