import urllib
from bs4 import BeautifulSoup
import ssl
import WebScraperJSON


class ShopifyPageParser:
    def __init__(self, url):
        self.new_url = url
        self.pages = []
        self.links = []

    # returns all the pages of items with the last item being the original url
    def find_pages(self, new_url):
        return_array = []
        for page in range(1, 10):
            url = new_url + '?page=' + str(page)
            return_array.append(url)
        original_url = new_url.split('/')
        return_array.append("https://" + original_url[2])
        self.pages = return_array
        return return_array

    # returns all the links to items on the page
    def find_links(self, page_url, origin):
        ssl_thing = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        return_string = []
        for pages in page_url:
            html = urllib.request.urlopen(pages, context=ssl_thing)
            soup = BeautifulSoup(html, 'lxml')
            for item in soup.findAll('a', class_='product-block__title-link'):
                return_string.append(origin + item['href'])
        self.links = return_string
        return return_string

    # returns links to all individual items on a site, calls the other methods in class
    def parse_shopify(self):
        pages_of_site = ShopifyPageParser.find_pages(self, self.new_url)
        original_url = pages_of_site[-1]
        pages_of_site = pages_of_site[:-1]
        page_links = ShopifyPageParser.find_links(self, pages_of_site, original_url)
        return page_links

    # returns the name of all the items on the site
    def item_name(self):
        return_array = []
        for link in ShopifyPageParser.parse_shopify(self):
            return_array.append(WebScraperJSON.item_name(link))
        return return_array

    # returns the name of all the items on the site
    def item_options(self):
        return_array = []
        for link in ShopifyPageParser.parse_shopify(self):
            item = WebScraperJSON.item_options(link)
            if item not in return_array:
                return_array.append(WebScraperJSON.item_options(link))
        return return_array












