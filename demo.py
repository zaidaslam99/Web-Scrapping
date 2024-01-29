from bs4 import BeautifulSoup
import requests
import time 

print("\nPut some skills that you are not familiar with: ")
unfamiliar_skill_list = input("Enter the skills: ")

def find_jobs():
    # We need to scrape from a website using requests
    html_text = requests.get("https://www.indeed.com/jobs?q=python&l=Sugar+Land%2C+TX&from=searchOnHP&vjk=333429c6fc5d84d6")
    
    # We need to use LXML parser to break apart html
    soup = BeautifulSoup(html_text, "lxml")
    
    
    # Following Pagination we need first page
    jobs = soup.find_all("li", class_="css-5lfssm eu4oa1w0")
    
    print(jobs)