from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

def get_art_text(link):

    r = BeautifulSoup(requests.get(link).text)

    content = r.find('div', {"class": "article-restofcontent"})

    text = [p.text for p in content.find_all("p", {"class": "article__body"})]

    return "\t".join(text)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        result = get_art_text(url)
        return render_template('result.html', result=result)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()