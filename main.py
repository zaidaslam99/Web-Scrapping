from bs4 import BeautifulSoup

with open("home.html", "r") as html_file:
    
    content = html_file.read()

    # lmxl is used to generate the html file
    soup = BeautifulSoup(content, "lxml")
    
    # Here we are using div and filtering each div 
    # class_ is used to identify class since class is built in python we cant use it by itself
    course_cards = soup.find_all("div", class_="card")
    for course in course_cards:
        course_name = course.h5.text
        # Will get text into a list
        course_price = course.a.text.split()[-1]
        
        print(f"{course_name} costs {course_price}")        
        # print(course.h5)
    
    # tags = soup.find("h5")
    # Finds all h5 elements puts them in a list
    # courses_html_tags = soup.find_all("h5")
    # for course in courses_html_tags:
    #     print(course.text)
        
