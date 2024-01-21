from bs4 import BeautifulSoup
import requests


html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=28").text
soup = BeautifulSoup(html_text, "lxml")
jobs = soup.find_all("li", class_ = "clearfix job-bx wht-shd-bx")
print(jobs)