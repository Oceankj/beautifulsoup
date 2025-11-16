# Milestone-3

### Test cases for new API
- `bs4/tests/test_filter.py`: lines 661–744
- `bs4/tests/test_soup.py`: lines 640–695


### How to run?
```
cd apps/m3
```

```
python task7.py file_name
```
---
### class SoupReplacer

SoupReplacer provides tag and attribute transformation for BeautifulSoup parse tree nodes.

It supports three types of transformers:

- `name_xformer`: Callable that transforms tag names.
- `attrs_xformer`: Callable that transforms tag attribute dictionaries.
- `xformer`: Callable applied to the Tag after it is fully constructed.


**NOTE REGARDING `xformer` AND USE WITH Tag.string:**
- Avoid mutating `tag.string` directly, as `Tag.string` is a property that *recursively* returns a NavigableString from a descendant if the tag's only child is itself a Tag with string content. Modifying `tag.string` may inadvertently impact nested tags' contents or result in multiple transformations of the same NavigableString.
- Instead, always operate on direct children:
  - Traverse `tag.contents` and test for `isinstance(child, NavigableString)`.
  - Use `child.replace_with(NavigableString(...))` or create a new NavigableString and replace it in place. This avoids altering descendants unintentionally and ensures you only modify strings directly owned by the `Tag`.

Example (correct usage for string transformation):
```python
def safe_xformer(tag):
    for child in tag.contents:
        if isinstance(child, NavigableString):
            child.replace_with(NavigableString(child.upper()))
```

## Usage Examples

### 1. Change tag names conditionally

Replace every `<b>` with `<blockquote>`, leave other tags unchanged:

```python
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer

html_doc = "<div><b>Bold</b> and <i>Italic</i></div>"
replacer = SoupReplacer(
    name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name
)
soup = BeautifulSoup(html_doc, replacer=replacer, features="lxml")
print(soup)
# Output: <div><blockquote>Bold</blockquote> and <i>Italic</i></div>
```

### 2. Remove a specific attribute from all tags

Remove the `class` attribute from all elements:

```python
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer

def remove_class_attr(tag):
    if "class" in tag.attrs:
        del tag.attrs["class"]

html_doc = '<div class="outer"><span class="foo" id="s1">Hello</span><b>NoClass</b></div>'
replacer = SoupReplacer(xformer=remove_class_attr)
soup = BeautifulSoup(html_doc, replacer=replacer, features="lxml")
print(soup)
# Output: <div><span id="s1">Hello</span><b>NoClass</b></div>
```

### 3. Transform both tag names and attributes

Prefix tag names with `"x-"` and rename attribute `"foo"` to `"bar"`:

```python
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer

def name_xformer(tag):
    return "x-" + tag.name

def attrs_xformer(tag):
    attrs = tag.attrs
    if "foo" in attrs:
        attrs["bar"] = attrs.pop("foo")
    return attrs

markup = '<root><child foo="val">text</child></root>'
replacer = SoupReplacer(name_xformer=name_xformer, attrs_xformer=attrs_xformer)
soup = BeautifulSoup(markup, replacer=replacer, features="lxml-xml")
print(soup)
# Output: <x-root><x-child bar="val">text</x-child></x-root>
```

### 4. Advanced: Custom transformer for tag names and string content

Uppercase all tag names and reverse text content of direct string children:

```python
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer
from bs4.element import NavigableString

def name_xformer(tag):
    return tag.name.upper()

def xformer(tag):
    # Only operate on direct NavigableString children
    for child in tag.contents:
        if isinstance(child, NavigableString):
            child.replace_with(NavigableString(child[::-1]))

markup = "<doc><data>abc</data></doc>"
replacer = SoupReplacer(name_xformer=name_xformer, xformer=xformer)
soup = BeautifulSoup(markup, replacer=replacer, features="lxml-xml")
print(soup)
# Output: <DOC><DATA>cba</DATA></DOC>
```
