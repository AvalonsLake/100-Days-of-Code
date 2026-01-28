import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

# ========== Scraping the data ========== #
response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
movie_titles = soup.find_all("h3", class_="title")

movie_list = [movies.text for movies in movie_titles[::-1]]

print(movie_list)


# =========== Writing the list to a txt file ========== #
with open("best_movies.txt", "w", encoding="utf-8") as file:
    for movie in movie_list:
        file.write(movie + "\n")