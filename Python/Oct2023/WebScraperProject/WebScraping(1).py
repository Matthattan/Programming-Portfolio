from bs4 import BeautifulSoup
import os

# Get the directory of the current Python file/HTML file
current_directory = os.path.dirname(os.path.abspath(__file__))
html_filename = "index.html"
html_filepath = os.path.join(current_directory, html_filename)

# Open HTML File
with open(html_filepath, "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# Print HTML file with indetation
print(doc.prettify())

# locate the first h1 tag 
# <h1>Welcome to the Mock Website</h1>
tag = doc.h1

# print only the text inside the tag
print(tag.string)

# change string inside h1 tag
tag.string = "Hello World!"
print(doc)

# finding p tags other than the first instance
tags = doc.find_all("p")

# finding the (second) p tag
specificTag = doc.find_all("p")[1]
print(tags)
print(specificTag)



