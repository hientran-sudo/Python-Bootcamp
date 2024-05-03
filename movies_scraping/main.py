from bs4 import BeautifulSoup
import requests

response = requests.get(
    "https://www.empireonline.com/movies/features/best-movies-2/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
all_movies = soup.find_all(name="h3",
                           class_="listicleItem_listicle-item__title__BfenH")

movies_titles = [movie.getText() for movie in all_movies]
# reverse the order 1 to 100 instead of 100 to 1
movies = movies_titles[::-1]
print(movies)

with open("movie.txt", mode="w") as file:
  for movie in movies_titles:
    file.write(movie + "\n")
