# Scrape-Movies
Python program that writes a list of the top must-watch movies as text file.

The program will read and parse a webpage (namely, https://www.timeout.com/newyork/movies/best-movies-of-all-time) as HTML.
Then, we tap into the HTML and search for the movie titles listed in the soup ( the HTML code we just parsed).
These titles are inside anchor tags nested in h3 tags and stored as list in a variable

Using the "select()" method, we tap into the text inside these anchor tags with the mehtod "getText()" and do a bit of string manipulation.
We append the resulting string into a list.

Of coure this occurs inside a for loop that is looping over all the anchor tags found.

The list containing our movie titles is then use to write into a file "movies.txt" the names of all the titles any cinema afficionado should watch !
