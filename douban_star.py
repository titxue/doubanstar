from urllib import request
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
url = "https://movie.douban.com/top250"
# 设置headers
req = request.Request(url=url, headers=self.headers)
res = request.urlopen(req)
contnet = res.read().decode("utf-8")
obj = BeautifulSoup(contnet,"html5lib")
results = obj.findAll("li")

for result in results:
    items = result.findAll("div",class_="item")
    stars = result.findAll("div", class_="star")
    for star in stars:
        score,voters = list(star.stripped_strings)
        print("- 评分：{}\n- 评价人数：{}".format(score, voters))
    for item in items:
        a = item.a
        img = a.img
        #标题
        title = img.get("alt")
        #封面
        cover = img.get("src")
        #地址
        address = a.get("href")
        #评分
        print("- 标题：{}\n- 封面：{}\n- 访问地址：{}\n{}".format(title,cover,address,"-"*100))
