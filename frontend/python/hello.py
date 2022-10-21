import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://test:1234@Cluster0.tmrbb2j.mongodb.net/?retryWrites=true&w=majority')
db = client.testC

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작

# title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
# print(title.text)
movies = soup.select('#old_content > table > tbody > tr')
for movie in movies:
    a = movie.select_one('td.title > div > a')
    if a is not None:
        title = a.text
        star = movie.select_one('td.point').text
        rank = movie.select_one('td:nth-child(1) > img')['alt']
        doc = {
            'title' : title,
            'rank' : rank,
            'star' : star,
        }
        
        db.movies.insert_one(doc)
# print(movies)
