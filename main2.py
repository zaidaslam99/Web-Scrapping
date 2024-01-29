from bs4 import BeautifulSoup
import requests
import time

print("\nPut some skills that you are not familiar with:")
unfamiliar_skill = input("Enter the skills: ")

def find_jobs():
    # Here we are getting the html text from the website
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=").text

    # Here we are going to be using an lxml parser
    soup = BeautifulSoup(html_text, "lxml")

    # Brings results for the first page 
    jobs = soup.find_all("li", class_ ='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):

        # Since span is within another span we need to access the element
        # So outer container then span tag then text
        published_date = job.find('span', class_ = "sim-posted").span.text
        
        if "few" in published_date:
            # We are going to get the text for h3
            company_name = job.find("h3", class_ = "joblist-comp-name").text.replace(" ", "")
            skills = job.find("span", class_ = "srp-skills").text.replace(" ", "")
            more_info = job.header.h2.a["href"]
            if unfamiliar_skill not in skills:
                # Display results 
                with open(f"posts/{index}.txt", "w") as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info} \n")
                print(f"File saved: {index}")
if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)
        