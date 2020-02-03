#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup as soup


class Node(object):
    def __init__(self, val=None, parent=None, children=None, **kwargs):
        self.val = val
        self.parent = parent
        self.children = children if isinstance(children, list) else []
        super(object, self).__init__(**kwargs)

    def __str__(self):
        return self.val.__str__()

    def __repr__(self):
        return '<Node %r>' % self.val

    def __dir__(self):
        """
        Defines behavior for when dir() is called on an instance of
        a 'Node'. This method should return a list of attributes for
        the user. Typically, implementing __dir__ is unnecessary, but
        it can be vitally important for interactive use of your
        classes if you redefine __getattr__ or __getattribute__ or
        are otherwise dynamically generating attributes.
        """
        return

    def __nonzero__(self):
        """
        Defines behavior for when bool() is called on an instance
        of a 'Node'. Should return True or False, depending on
        whether you would want to consider the instance to be True
        or False.
        """
        return len(self.children) >= 1

    def __getitem__(self, key):
        raise NotImplementedError

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __delitem__(self, key):
        raise NotImplementedError

    def __len__(self):
        return len(self.children)

    def __iter__(self):
        return iter(self.children)

    def __reversed__(self):
        return reversed(self.children)

    def append(self, child):
        self.children.append(child)

    def head(self):
        return self.children[0]

    def tail(self):
        return self.children[1:]

    def init(self):
        return self.children[:-1]

    def last(self):
        return self.children[-1]

    def drop(self, n):
        return self.children[n:]

    def take(self, n):
        return self.children[:n]


class Bill:
    link = ""
    title = ""
    sponsor = {
        'name': "",
        'link': ""
    }
    introduced = ""
    cosponsors = {
        'link': "",
        'all': [
            {
                'name': "",
                'link': ""
            }
        ]
    }
    committees = ""
    latest_action = ""
    all_actions_link = ""
    tracker = {
        'introduced': True,
        'Passed House': False,
        'Passed Senate': False,
        'To President': False,
        'Became Law': False
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def main():

    def getSoup(url):

        raw_html = requests.get(url)

        return soup(raw_html.content, "html.parser")

    # def getBillsOnPage():
    url = "https://www.congress.gov/search?pageSize=100&page=2"
    # url = "https://www.congress.gov/search?pageSize=250&page=2"
    # url = "https://www.congress.gov/search?pageSort=dateOfIntroduction%3A" + "desc" if True else "asc" + "&s=2&q=%7B%22congress%22%3A%22all%22%2C%22source%22%3A%22all%22%7D&pageSize=250&page=2"
    print('url: ' + url)

    root_soup = getSoup(url)

    main = root_soup.find("div", attrs={'id': 'main'})

    bill_data_containers = main.findAll("li", attrs={'class': 'compact'})
    print("len(bill_data_containers): " + str(len(bill_data_containers)))

    bill_data_links = [bill_data_container.a.get('href') for bill_data_container in bill_data_containers]
    print('bill_main_links[0]: ' + str(bill_data_links[0]))

    bill_data_titles = [bill_data_container.find("span", attrs={'class': 'result-title'}).text for bill_data_container in bill_data_containers]
    print('bill_data_titles[0]: ' + str(bill_data_titles[0]))

    bill_data_sponsor = [bill_data_container.findAll("span", attrs={'class': 'result-item'})[0].span.a.text for bill_data_container in bill_data_containers]
    print('bill_data_sponsor[0]: ' + str(bill_data_sponsor[0]))

    bill_data_sponsor_links = ["https://www.congress.gov" + bill_data_container.findAll("span", attrs={'class': 'result-item'})[0].span.a.get('href') for bill_data_container in bill_data_containers]
    print('bill_data_sponsor_links[0]: ' + str(bill_data_sponsor_links[0]))

    bill_data_introduced = [str(bill_data_container.findAll("span", attrs={'class': 'result-item'})[0].span.a.nextSibling)[13:-2] for bill_data_container in bill_data_containers]
    print('bill_data_introduced[0]: ' + str(bill_data_introduced[0]))

    bill_data_cosponsors_counts = [bill_data_container.findAll("span", attrs={'class': 'result-item'})[0].findAll('a')[1].text for bill_data_container in bill_data_containers]
    print('bill_data_cosponsors_counts[0]: ' + str(bill_data_cosponsors_counts[0]))

    bill_data_cosponsors_links = [bill_data_container.findAll("span", attrs={'class': 'result-item'})[0].findAll('a')[1].get('href') for bill_data_container in bill_data_containers]
    print('bill_data_cosponsors_links[0]: ' + str(bill_data_cosponsors_links[0]))

    bill_data_committees = [bill_data_container.findAll("span", attrs={'class': 'result-item'})[1].span.text for bill_data_container in bill_data_containers]
    print('bill_data_committees[0]: ' + str(bill_data_committees[0]))

    bill_data_latest_action = [bill_data_container.findAll("span", attrs={'class': 'result-item'})[2].span.a.previousSibling for bill_data_container in bill_data_containers]
    print('bill_data_latest_action[0]: ' + str(bill_data_latest_action[0]))

    bill_data_all_actions_links = [bill_data_container.findAll("span", attrs={'class': 'result-item'})[2].span.a.get('href') for bill_data_container in bill_data_containers]
    print('bill_data_all_actions_links[0]: ' + str(bill_data_all_actions_links[0]))

    # # getBillsOnPage(1)
    # getBillsOnPage()


if __name__ == "__main__":
    main()
