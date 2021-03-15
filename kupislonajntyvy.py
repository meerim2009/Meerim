from bs4 import BeautifulSoup
import requests
url = "https://kupislona.kg"
response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")
reviews = soup.find("div", {"class": "container-fluid otzyvy-main"}).findChildren("div", {"class": "cont"})

for i in reviews:
    name = i.find("div", {"class": "title"}).text
    review = i.find("div", {"class": "text"}).text
    print(f"Name: {name}\nReview: {review}\n")
