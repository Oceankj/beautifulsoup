# Replace specific tag and print out all the tags in the document.
import sys
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer

file_name = sys.argv[1]
parser = ""
replace_row_to_col = SoupReplacer("row", "col")


def get_parser(file_name):
    if file_name.endswith(".html"):
        return "lxml"
    elif file_name.endswith(".xml"):
        return "lxml-xml"
    else:
        raise ValueError("Unsupported file extension: {}".format(file_name))


with open(file_name) as fr:
    file_content = fr.read()
    soup = BeautifulSoup(
        file_content, get_parser(file_name), replacer=replace_row_to_col
    )

print(soup.prettify())
