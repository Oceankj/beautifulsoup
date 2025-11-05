# Find all the <p> tags and add (or replace) a class attribute class="test"
# then write the tree onto a file.

import sys
from typing import cast
from bs4 import BeautifulSoup, SoupReplacer, Tag
from bs4.element import AttributeValueList

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


def attrs_xformer(tag: "Tag"):
    if tag.name != "p":
        return tag.attrs

    new_attrs = dict(tag.attrs)

    if "class" in new_attrs:
        class_value = new_attrs["class"]
        class_list = class_list = AttributeValueList(
            [class_value] if isinstance(class_value, str) else class_value
        )

        if "test" not in class_list:
            class_list.append("test")

        new_attrs["class"] = class_list
    else:
        new_attrs["class"] = AttributeValueList(["test"])

    return new_attrs


replacer = SoupReplacer(attrs_xformer=attrs_xformer)
soup: BeautifulSoup = BeautifulSoup(file_content, parser, replacer=replacer)

with open(file_name, "w") as fw:
    fw.write(cast(str, soup.prettify()))
