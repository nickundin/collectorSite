from bs4 import BeautifulSoup
import NormalPage
import requests
import TabsPage
import concurrent.futures

linkList = ["https://www.ebay.com/itm/393617426516?_trkparms=amclksrc%3DITM%26aid%3D111001%26algo%3DREC.SEED%26ao%3D1%26asc%3D20180816085401%26meid%3D2a3254eaf722450eae41b3dbd6e6bea3%26pid%3D100970%26rk%3D2%26rkt%3D15%26sd%3D334158435848%26itm%3D393617426516%26pmt%3D0%26noa%3D1%26pg%3D2380057%26brand%3DFunko&_trksid=p2380057.c100970.m5481&_trkparms=pageci%3A0ef1e5d7-294c-11ec-a343-96fa9191fbd3%7Cparentrq%3A6710ad0c17c0a9fc3c1d72d0fffb4d19%7Ciid%3A1", "https://www.ebay.com/itm/224586751195?_trkparms=amclksrc%3DITM%26aid%3D777008%26algo%3DPERSONAL.TOPIC%26ao%3D1%26asc%3D20200708143445%26meid%3D5597586e56fd4c85a8f28bfdf214fb81%26pid%3D101251%26rk%3D1%26rkt%3D1%26itm%3D224586751195%26pmt%3D1%26noa%3D1%26pg%3D2380057%26algv%3DPersonalizedTopicsV2WithMLR%26brand%3DFunko&_trksid=p2380057.c101251.m47269&_trkparms=pageci%3A0ef1e5d7-294c-11ec-a343-96fa9191fbd3%7Cparentrq%3A6710ad0c17c0a9fc3c1d72d0fffb4d19%7Ciid%3A1", "https://www.ebay.com/itm/324793977246?_trkparms=amclksrc%3DITM%26aid%3D777008%26algo%3DPERSONAL.TOPIC%26ao%3D1%26asc%3D20200708143445%26meid%3D5597586e56fd4c85a8f28bfdf214fb81%26pid%3D101251%26rk%3D1%26rkt%3D1%26itm%3D324793977246%26pmt%3D1%26noa%3D1%26pg%3D2380057%26algv%3DPersonalizedTopicsV2WithMLR%26brand%3DFunko&_trksid=p2380057.c101251.m47269&_trkparms=pageci%3A0ef1e5d7-294c-11ec-a343-96fa9191fbd3%7Cparentrq%3A6710ad0c17c0a9fc3c1d72d0fffb4d19%7Ciid%3A1"]


class PageParser:
    def __init__(self, url):
        self.url = url

    # returns all the pages of items with the last item being the original url
    def find_pages(self, url):
        return_array = []
        for page in range(1, 2):
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
    def parse_pages(self):
        pages_of_site = PageParser.find_pages(self, self.url)
        page_links = PageParser.find_links(self, pages_of_site)
        return page_links

    def test(self, link):
        print(link)
        soup = NormalPage.turn_to_soup(link)
        if soup.find("ul", class_="themes-panel") is not None \
                or soup.find("div", class_="app-mtp-theme-tabs") is not None:
            print("tabs page")
            product_attributes = TabsPage.item_attributes(soup)
            print(product_attributes)
            return product_attributes
        else:
            print("normal page")
            product_attributes = NormalPage.item_attributes(soup)
            print(product_attributes)
            return product_attributes

    def parse_all(self):
        with concurrent.futures.ProcessPoolExecutor() as executor:
            return_array = executor.submit(PageParser.test, linkList[0])
        return return_array


def testing(url):
    soup = NormalPage.turn_to_soup(url)
    if soup.find("ul", class_="themes-panel") is not None \
            or soup.find("div", class_="app-mtp-theme-tabs") is not None:
        print("tabs page")
        product_attributes = TabsPage.item_attributes(url)
        print(product_attributes)
    else:
        print("normal page")
