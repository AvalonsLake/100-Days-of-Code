import spotipy
import requests
from bs4 import BeautifulSoup

date = input("What year would you like to travel to? Type the date in this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

data = requests.get(f"https://www.billboard.com/charts/hot-100/{date}", headers=header)

soup = BeautifulSoup(data.text, "html.parser")

song_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_spans]

print(song_names)

# ========== Spotify Functionality and Implementation ========== #

# needs
# Search for songs -
# add items to playlist - https://spotipy.readthedocs.io/en/2.25.2/#spotipy.client.Spotify.playlist_add_items
# tracks section - https://spotipy.readthedocs.io/en/2.25.2/#spotipy.client.Spotify.tracks



# ========== Writes the data from Response into a txt file as a top 100 list ========== #

with open(f"{date}.txt", "w") as file:
    i=0
    for song in song_names:
        i = i+1
        file.write(f"{i}) {song}\n")