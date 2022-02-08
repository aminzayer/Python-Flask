from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import urllib
from flask import Flask
from flask import jsonify
import re


app = Flask(__name__)
#app.config["DEBUG"] = True


def google_result():
    keyword = "Amin Zayeromali"
    html_keyword = urllib.parse.quote_plus(keyword)
    #print(html_keyword)

    number_of_result = 20
    google_url = "https://www.google.com/search?q=" + \
        html_keyword + "&num=" + str(number_of_result)
    #print(google_url)

    ua = UserAgent()
    response = requests.get(google_url, {"User-Agent": ua.random})
    soup = BeautifulSoup(response.text, "html.parser")

    result = soup.find_all('div', attrs={'class': 'ZINbbc'})
    results = [re.search('\/url\?q\=(.*)\&sa', str(i.find('a', href=True)['href']))for i in result if "url" in str(i)]
    #this is because in rare cases we can't get the urls
    links = [i.group(1) for i in results if i != None]
    #print(links)

    return links


@app.route('/')
def Webservice_index():
    return 'Google Links of Result Web Service.'


@app.route("/google")
def google():
    links = google_result()
    json_format = jsonify({'link':links})
    return json_format


app.run()