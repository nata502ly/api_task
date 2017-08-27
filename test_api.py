import requests
from lxml.html import fromstring
from bs4 import BeautifulSoup



address_list = ["http://github.com/",
                "https://github.com/",
                "https://www.github.com/",
                "https://www.github.com/test/",
                "https://github.com/testlololo",
                "https://github.com/test?lol"]
answers = [307, 200, 301, 301, 404, 200]
status_code = [requests.get(item).status_code for item in address_list]
print(answers, status_code)
index = [0,1,2,3,4,5]
for i in index:
    if answers[i] == status_code[i]:
        print("Success")
    else:
        print("Failed")
for a in status_code:
    if status_code == 200:
        tree = fromstring(a.content)
        title = tree.findtext('.//title')
        soup = BeautifulSoup(a.text)
        metas = soup.find_all('meta')
        get_text = a.text
        soup = BeautifulSoup(get_text, "html.parser")
        b = soup.find_next('h1', 'class:listing-name')
        print(title, metas, b)
