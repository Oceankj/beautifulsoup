# Find all the <p> tags and add (or replace) a class attribute class="test"
# then write the tree onto a file.

import sys
from bs4 import BeautifulSoup

file_name = sys.argv[1]
parser = ""
file_content = ""

with open(file_name) as fr:
    if file_name.endswith(".html"):
        parser = "lxml"
    elif file_name.endswith(".xml"):
        parser = "lxml-xml"
    else:
        raise ValueError("Unsupported file extension: {}".format(file_name))
    file_content = fr.read()


soup: BeautifulSoup = BeautifulSoup(file_content, parser)


for node in soup:
    print(node)
    print("------")
