from bs4 import BeautifulSoup

with open("D:\\Visual Studio Codes\\Beautiful Soup Free Code Camp\\web scrapping\\home.html", "r") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "lxml") 

course_cards = soup.find_all("div", class_="card")

for course in course_cards:
    # print(course)  
    
    course_name = course.h5.text.strip() # Extract the course name from the h5 tag
    course_price = course.a.text.strip()
    print(course_name)
    print(f"{course_price}\n") 
     
    # print(course.h5.text)  # Print the text content of each course card
    # print(course.text)  # Print the text content of each course card
    
    # print(course.text.strip())  # Print the text content of each course card
    # print("-----")  # Separator for readability