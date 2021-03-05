from bs4 import BeautifulSoup
import requests

url = "https://24.kg"
response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")
last_news_list = soup.find("div", {"class": "row lineNews"}).findChildren("div", {"class": "one"})

class Article:
    def get_last_news(self):
        newsMass = []
        for new in last_news_list:
            time = new.find("div", {"class": "time"})
            title = new.find("div", {"class": "title"})
            link = new.find("a").attrs["href"]
            newsMass.append({"time": time.text, "title": title.text, "link": url + link})
        return newsMass

    def parse_detail_info(self, url):
        responseDetail = requests.get(url).text
        soupDetail = BeautifulSoup(responseDetail, "html.parser")
        details = soupDetail.find("div", {"class": "cont"}).text
        return details

    def get_html(self, url):
        responsehtml = requests.get(url).text
        return responsehtml



newsArtile = Article().get_last_news()
detail = Article().parse_detail_info(newsArtile[0]["link"])
html = Article().get_html("https://google.com")
print(html)