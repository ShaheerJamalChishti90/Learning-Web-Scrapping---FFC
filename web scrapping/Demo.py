from bs4 import BeautifulSoup


with open("D:\\Visual Studio Codes\\Beautiful Soup Free Code Camp\\web scrapping\\home.html", "r") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "lxml") # or "html.parser"/this will parse the file in lxml format

# print(soup.prettify()) # this will print the file in a readable format

# tags = soup.find_all("a") # this will find all the tags in the file

# tags = soup.find("h1") # this will find the first  occourence of h1 tag in the file

tags = soup.find_all("h5") # this will find all the tags in the file
# print(tags) # this will print the tags in the file

#we can only print the course attribute like this
for i in tags:
    print(i.text) 