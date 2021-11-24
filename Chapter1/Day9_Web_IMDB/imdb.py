import requests
from bs4  import BeautifulSoup

html_text=requests.get("https://www.imdb.com/list/ls009668711/").text
#print(html_text)
soup = BeautifulSoup(html_text,'html.parser')
list=soup.find('div',class_="lister-item mode-detail")

movie_name=list.find('h3',class_='lister-item-header').text
print(movie_name)
Description=list.find_all('p')[1].get_text()
print(Description)
rating=list.find('span',class_='ipl-rating-star__rating').text
print(rating)
Directors=list.find_all('p')[2].get_text()
print(Directors)
votes=list.find('span',name='nv').text
print(votes)
#Gross=list.find('span',class_='')