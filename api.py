import requests
from lxml.html import fromstring
from bs4 import BeautifulSoup

r = requests.get("http://github.com/")
print(r.status_code)
if r.status_code == 200:
    tree = fromstring(r.content)
    a = tree.findtext('.//title')
    soup = BeautifulSoup(r.text)
    metas = soup.find_all('meta')
    get_text = r.text
    soup = BeautifulSoup(get_text, "html.parser")

    b = soup.find_next('h1', 'class:listing-name')
    print(a, metas, b)
r = requests.get("https://github.com/")
print(r.status_code)
if r.status_code == 200:
    tree = fromstring(r.content)
    a = tree.findtext('.//title')
    soup = BeautifulSoup(r.text)
    metas = soup.find_all('meta')
    get_text = r.text
    soup = BeautifulSoup(get_text, "html.parser")

    b = soup.find_next('h1', 'class:listing-name')
    print(a, metas, b)
r = requests.get("https://www.github.com/")
print(r.status_code)
if r.status_code == 200:
    tree = fromstring(r.content)
    a = tree.findtext('.//title')
    soup = BeautifulSoup(r.text)
    metas = soup.find_all('meta')
    get_text = r.text
    soup = BeautifulSoup(get_text, "html.parser")

    b = soup.find_next('h1', 'class:listing-name')
    print(a, metas, b)
r = requests.get("https://www.github.com/test/")
print(r.status_code)
if r.status_code == 200:
    tree = fromstring(r.content)
    a = tree.findtext('.//title')
    soup = BeautifulSoup(r.text)
    metas = soup.find_all('meta')
    get_text = r.text
    soup = BeautifulSoup(get_text, "html.parser")

    b = soup.find_next('h1', 'class:listing-name')
    print(a, metas, b)
r = requests.get("https://github.com/testlololo")
print(r.status_code)
if r.status_code == 200:
    tree = fromstring(r.content)
    a = tree.findtext('.//title')
    soup = BeautifulSoup(r.text)
    metas = soup.find_all('meta')
    get_text = r.text
    soup = BeautifulSoup(get_text, "html.parser")

    b = soup.find_next('h1', 'class:listing-name')
    print(a, metas, b)
r = requests.get("https://github.com/test?lol")
print(r.status_code)
if r.status_code == 200:
    tree = fromstring(r.content)
    a = tree.findtext('.//title')
    soup = BeautifulSoup(r.text)
    metas = soup.find_all('meta')
    get_text = r.text
    soup = BeautifulSoup(get_text, "html.parser")

    b = soup.find_next('h1', 'class:listing-name')
    print(a, metas, b)


