from bs4 import BeautifulSoup
import os
import re

# Get the directory of the current Python file/HTML file
current_directory = os.path.dirname(os.path.abspath(__file__))
html_filename = "complexWebsite.html"
html_filepath = os.path.join(current_directory, html_filename)

with open(html_filepath, "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# first instance of h3
tag = doc.find("h3")
# print(tag.attrs)

# change the style property inside tag
tag['style'] = 'color: orangered;'

# add a property to the tag
tag['font-weight'] = 'bold'
# print(tag)

# finding multiple tags (and children) with find_all
tags = doc.find_all(["p", "div", "li"], )
# print(tags)

# finding tags that meet a certain condition with text inside and relevant attributes
specificTag = doc.find_all(["p"], string="Some content for Article 2.2.", style="color: green;")
#print(specificTag)

# searching with classes
classTags = doc.find_all(class_="class1")
#print(classTags)

# using regex to find values
regexTag = doc.find_all(string=re.compile("Article.*"), limit=2)
for tag in regexTag:
    print(tag.strip())