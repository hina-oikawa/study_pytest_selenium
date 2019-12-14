import requests
from bs4 import BeautifulSoup

requestsData = requests.get('https://news.yahoo.co.jp')
soup = BeautifulSoup(requestsData.content, "html.parser")
print(soup.find("ul", "newsFeed_list").text)

print(requestsData.headers)
print("-------------------")
print(requestsData.encoding)
print(requestsData.content)


html = "<h1>sayhello</h1>,<h1>saysay</h1>,<h2>say</h2>"
soup = BeautifulSoup(html, "html.parser")
print(soup.select("h1"))
