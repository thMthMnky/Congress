#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup as soup


# my_url = "https://www.congress.gov/search?q=%7B%22subject%22%3A%22Crime+and+Law+Enforcement%22%7D&searchResultViewType=expanded&KWICView=false&pageSize=100&page=1"
# my_url = "https://www.congress.gov/search?q={%22subject%22:%22Crime+and+Law+Enforcement%22}&pageSize=100&page=2&searchResultViewType=expanded&KWICView=false"
my_url = "https://www.congress.gov/search?pageSort=dateOfIntroduction:desc&searchResultViewType=compact"

raw_html = requests.get(my_url)

root = soup(raw_html.content, "html.parser")

main = root.find("div", attrs={'id': 'main'})

bill_roots = main.findAll("span", attrs={'li': 'compact'})


class Node(object):
    def __init__(self, val=None, parent=None, children=None, *args, **kwargs):

        self.type = str
        for key, value in kwargs.items():
            if key == 'type':
                if set((value)) <= set((str, object)):
                    self.type = value
                else:
                    raise TypeError("Can not instantiate a 'Node' of type: " + value)

        self.val = val if val is not None and isinstance(val, self.type) else str(val)
        self.parent = parent if parent is not None and isinstance(parent, list) else []
        self.children = children if children is not None and isinstance(children, list) else []
        super(object, self).__init__(*args, **kwargs)

    def __str__(self):
        """
        Defines behavior for when str() is called on an instance of a 'Node'.
        """
        return self.val.__str__()

    def __repr__(self):
        """
        Defines behavior for when repr() is called on an instance
        of a 'Node'. The major difference between str() and repr()
        is intended audience. repr() is intended to produce output
        that is mostly machine-readable (in many cases, it could
        be valid Python code even), whereas str() is intended to
        be human-readable.
        """
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
        pass

    def __sizeof__(self):
        """
        Defines behavior for when sys.getsizeof() is called on an
        instance of a 'Node'. This should return the size of
        your object, in bytes. This is generally more useful
        for Python classes implemented in C extensions,
        but it helps to be aware of it.
        """
        pass

    def __nonzero__(self):
        """
        Defines behavior for when bool() is called on an instance
        of a 'Node'. Should return True or False, depending on
        whether you would want to consider the instance to be True
        or False.
        """
        pass

    def __len__(self):
        return len(self.val)

    def __getitem__(self, key):
        # if key is of invalid type or value, the list values will raise the error
        return self.val[key]

    def __setitem__(self, key, value):
        self.val[key] = value

    def __delitem__(self, key):
        del self.val[key]

    def __iter__(self):
        return iter(self.val)

    def __reversed__(self):
        return reversed(self.val)

    def append(self, val):
        self.val.append(val)

    def head(self):
        # get the first element
        return self.val[0]

    def tail(self):
        # get all elements after the first
        return self.values[1:]

    def init(self):
        # get elements up to the last
        return self.values[:-1]

    def last(self):
        # get last element
        return self.values[-1]

    def drop(self, n):
        # get all elements except first n
        return self.values[n:]

    def take(self, n):
        # get first n elements
        return self.values[:n]


class FunctionalList:
    '''A class wrapping a list with some extra functional magic, like head,
    tail, init, last, drop, and take.'''

bill_headers_a = [bill_header.a for bill_header in bill_roots]

bill_main_links = [bill_header.get('href') for bill_header in bill_headers_a]

nav = root.find("div", attrs={'id': 'nav'})

if __name__ == "__main__":
    # print("len(bill_headers): " + str(len(bill_headers)))
    # print("bill_headers[" + str(len(bill_headers) - 1) + "]: " + str(bill_headers[-1]))
    test_root = Node("some@cool.link")
    print(test_root)
    print("len(bill_main_links): " + str(len(bill_headers_a)))
    print("bill_main_links[0]: " + str(bill_headers_a[0]))
    print("len(bill_main_links): " + str(len(bill_main_links)))
    print("bill_main_links[0]: " + str(bill_main_links[0]))
