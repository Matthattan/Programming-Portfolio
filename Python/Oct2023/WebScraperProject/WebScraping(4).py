from bs4 import BeautifulSoup
import os

# Get the directory of the current Python file/HTML file
current_directory = os.path.dirname(os.path.abspath(__file__))
html1_filename = "complexWebsite.html"
html2_filename = "copiedWebsite.html"

html1a_filepath = os.path.join(current_directory, html1_filename)
html2a_filepath = os.path.join(current_directory, html2_filename)

# website to copy from
with open(html1a_filepath, "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tags = doc.find_all("p", class_="class2")
for tag in tags:
    tag["style"] = "color: pink;"

# website to paste into
with open(html2a_filepath, "w") as file:
    file.write(str(doc))


