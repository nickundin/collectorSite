from bs4 import BeautifulSoup
import requests
import time
import NormalPage


# get the name of the item
def item_name(input_url):
    soup = NormalPage.turn_to_soup(input_url)
    return soup.find("h1", class_="product-title").text


# getting the image
def item_image(input_url):
    soup = NormalPage.turn_to_soup(input_url)
    return soup.find("img", class_="vi-image-gallery__image vi-image-gallery__image--absolute-center")["src"]


# getting the price
def item_price(input_url):
    soup = NormalPage.turn_to_soup(input_url)
    return soup.find("div", class_="display-price").text


# getting the condition
def item_condition(input_url):
    soup = NormalPage.turn_to_soup(input_url)
    return soup.findAll("li", class_="item-highlight")[1].find("span").text


def item_seller(input_url):
    soup = NormalPage.turn_to_soup(input_url)
    return soup.find("div", class_="seller-persona").findAll("span")[1].find("a").text


def item_availability(input_url):
    soup = NormalPage.turn_to_soup(input_url)
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
    soup = NormalPage.turn_to_soup(input_url)
    return soup.findAll("li", class_="item-highlight")[2].text


def item_attributes(input_url):
    product = {"item_name": item_name(input_url), "item_image": item_image(input_url),
               "item_price": item_price(input_url), "item_condition": item_condition(input_url),
               "item_seller": item_seller(input_url), "item_availability": item_availability(input_url),
               "item return_policy": item_return_policy(input_url)}
    return product
