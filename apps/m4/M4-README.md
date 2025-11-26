# Milestone-4

### Test cases for new API
- `bs4/tests/test_soup.py`: lines 698-747

### How to Test
```
python -m pytest bs4/tests/test_soup.py::TestIterableSoup
```
---

### How to run?
```
cd apps/m4
```

```
python task.py file_name
```
---

### IterableSoup and Tag Iterable API

These test cases document and verify the iteration features of BeautifulSoup and Tag objects via their `__iter__` method, which provide depth-first traversal over the document tree.

#### Key behaviors:

- **Depth-First Iteration**:  
  - Calling `iter(soup)`, where `soup` is a BeautifulSoup object, yields the entire tree in depth-first order (document, then elements, including all tags and non-whitespace strings).

- **Iteration Includes Self**:  
  - Both `BeautifulSoup` and `Tag` objects, when iterated, yield themselves as the first item.
  Iterates over the document tree.

    >Note: In HTML parser, self-closing tags like <a/> are automatically converted to <a></a>, so traversal includes both the document node and the tag.


#### Example Usage

```python
soup = BeautifulSoup("<p>Hello <b>world</b>!</p>", "lxml")
for el in soup:
    print(el)

# the sequence yielded is:  
# "[document]", "p", "Hello ", "b", "world", "!"
```
This will print the `soup` object first, then descend into its tree, each node in depth-first order.


