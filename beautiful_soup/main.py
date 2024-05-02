from bs4 import BeautifulSoup
import lxml
with open("website.html") as file:
  contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup)

#format with identation, print the whole html content
print(soup.prettify())

print(soup.p)

anchor_tags = soup.find_all(name="a")
print(anchor_tags)
#print [<a href="www.google.com">Google</a>]

for tag in anchor_tags:
  print(tag.getText())
  print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

url = soup.select_one(selector="p a")
print(url)
#print <a href="https://www.appbrewery.co/">The App Brewery</a>

headings = soup.select(".heading")
print(headings)
#print <h3 class="heading">Books and Teaching</h3>
