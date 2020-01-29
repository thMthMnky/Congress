import requests
from bs4 import BeautifulSoup as soup
# https://www.congress.gov/search?q=%7B%22subject%22%3A%22Crime+and+Law+Enforcement%22%7D&searchResultViewType=expanded&KWICView=false&pageSize=100&page=1
my_url = "https://www.congress.gov/search?q={%22subject%22:%22Crime+and+Law+Enforcement%22}&pageSize=100&page=2&searchResultViewType=expanded&KWICView=false"
page_html = requests.get(my_url)
page_soup = soup(page_html.content, "html.parser")
main_container = page_soup.find("div", attrs={'id': 'main'})
bill_headers = main_container.findAll("span", attrs={'class': 'result-heading'})
if __name__ == "__main__":
    print(bill_headers)
