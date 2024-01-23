from bs4 import BeautifulSoup
import requests

# Here we are getting the html text from the website
html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=").text

# Here we are going to be using an lxml parser
soup = BeautifulSoup(html_text, "lxml")

# Brings results for the first page 
jobs = soup.find("li", class_ ='clearfix job-bx wht-shd-bx')

company_name = jobs.find("h3", class_ = "joblist-comp-name").text.replace(" ", "")
skills = jobs.find("span", class_ = "srp-skills")

print(skills)