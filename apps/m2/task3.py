# Print out all the tags in the document.
import sys
from bs4 import BeautifulSoup
from bs4.filter import SoupStrainer

file_name = sys.argv[1]
parser = ""
only_tag = SoupStrainer(True)


def get_parser(file_name):
    if file_name.endswith(".html"):
        return "lxml"
    elif file_name.endswith(".xml"):
        return "lxml-xml"
    else:
        raise ValueError("Unsupported file extension: {}".format(file_name))


with open(file_name) as fr:
    file_content = fr.read()
    soup = BeautifulSoup(file_content, get_parser(file_name), parse_only=only_tag)

for tag in soup.find_all():
    print(tag.name)
