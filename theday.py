import requests
from bs4 import BeautifulSoup

def get_art_text(link)

    r = BeautifulSoup(requests.get(link).text)

    content = r.find('div', {"class": "article-restofcontent"})

    text = [p.text for p in content.find_all("p", {"class": "article__body"})]

    return " ".join(text)