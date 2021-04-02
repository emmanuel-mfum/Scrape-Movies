from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.timeout.com/newyork/movies/best-movies-of-all-time")  # get request to the website

timeout_webpage = response.text  # get the text of the response
soup = BeautifulSoup(timeout_webpage, "html.parser")  # create a soup object with the response text and parse as html
movie_titles = []

titles = soup.select(selector="h3 a")  # selects all the h3 elements with an anchor element inside, returns a list of h3

for title in titles:  # for all elements in the list "titles"
    header = title.getText().strip()  # remove the new line and get the text inside the anchor tag

    movie_titles.append(header.replace("\xa0", " "))  # replaces the \xa0 with a space

print(movie_titles)

with open("movies.txt", 'w',encoding='utf-16') as file:  # create/write a new file with all the movie titles
    for movie in movie_titles:
        file.write(f"{movie}\n")
