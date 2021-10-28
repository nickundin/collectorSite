from bs4 import BeautifulSoup
import NormalPage
import collectorSite.WebScraper.NormalPage as NormalPage
# import NormalPage
# import TabsPage
import requests
import collectorSite.WebScraper.OtherPage as OtherPage
import collectorSite.WebScraper.TabsPage as TabsPage


class PageParser:
    def __init__(self, url):
        self.url = url

    # returns all the pages of items with the last item being the original url
    def find_pages(self, url, pages):
        return_array = []
        for page in range(1, pages):
            url = url + "?_pgn=" + str(page)
            return_array.append(url)
        return return_array

    # returns all the links to items on the page
    def find_links(self, page_url):
        return_string = []
        for pages in page_url:
            html = requests.get(pages).text
            soup = BeautifulSoup(html, 'lxml')
            for item in soup.findAll('a', class_="s-item__link"):
                return_string.append(item['href'])
        return return_string

    # returns links to all individual items on a site, calls the other methods in class
    def parse_pages(self, pages):
        pages_of_site = PageParser.find_pages(self, self.url, pages)
        page_links = PageParser.find_links(self, pages_of_site)
        return page_links

    # returns attributes of each item on the website
    def parse_all(self, pages):
        return_array = []
        for link in PageParser.parse_pages(self, pages):
            print(link)
            soup = NormalPage.turn_to_soup(link)
            # finds the type of page it is
            if soup.find("ul", class_="themes-panel") is not None \
                    or soup.find("div", class_="app-mtp-theme-tabs") is not None:
                print("tabs page")
                product_attributes = TabsPage.item_attributes(soup, link)
                # print(product_attributes)
                return_array.append(product_attributes)
            elif soup.find("h1", class_="product-title") is not None:
                print("Other Page")
                product_attributes = OtherPage.item_attributes(soup, link)
                # print(product_attributes)
                return_array.append(product_attributes)
            else:
                print("normal page")
                product_attributes = NormalPage.item_attributes(soup, link)
                # print(product_attributes)
                return_array.append(product_attributes)
        return return_array


def testing(url):
    soup = NormalPage.turn_to_soup(url)
    return OtherPage.item_attributes(soup, url)
