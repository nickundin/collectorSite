from WebPageWebScraper import PageParser
website = PageParser(
    'https://www.ebay.com/b/Collectible-Funko-Bobbleheads-1970-Now/149372/bn_3017826')
print(website.parse_all(2))
# print(WebPageWebScraper.testing("https://www.ebay.com/p/21049722604?iid=133908721446"))
