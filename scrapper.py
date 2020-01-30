import requests

from bs4 import BeautifulSoup as soup
# https://www.congress.gov/search?q=%7B%22subject%22%3A%22Crime+and+Law+Enforcement%22%7D&searchResultViewType=expanded&KWICView=false&pageSize=100&page=1
my_url = "https://www.congress.gov/search?q={%22subject%22:%22Crime+and+Law+Enforcement%22}&pageSize=100&page=2&searchResultViewType=expanded&KWICView=false"
page_html = requests.get(my_url)
page_soup = soup(page_html.content, "html.parser")
main_container = page_soup.find("div", attrs={'id': 'main'})
bill_headers = main_container.findAll("span", attrs={'class': 'result-heading'})
# bill_main_link = bill_headers.findAll("a", attrs={'':''})
if __name__ == "__main__":
    print("len(bill_headers): ", bill_headers.__len__())
    print("bill_headers[" + str(len(bill_headers) - 1) + "]: ", bill_headers[bill_headers.__len__()-1])
#    print("len(bill_main_link): " + len(bill_main_link))
