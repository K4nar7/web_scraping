import requests as req
from bs4 import BeautifulSoup 
import csv
from itertools import zip_longest

job_title = []
company_name = []
location_name = []
skills = []
links = []
# Get the page
result = req.get('https://wuzzuf.net/search/jobs/?a=navbg&q=python')

#save page content
src = result.content

#Create a soup object
soup  = BeautifulSoup(src, 'lxml')

job_titles = soup.find_all('h2',{'class':'css-m604qf'})
company_names = soup.find_all('a',{'class':'css-17s97q8'})
location_names = soup.find_all('span',{'class':'css-5wys0k'})
job_skills = soup.find_all('div',{'class':'css-y4udm8'})

for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    links.append(job_titles[i].find('a').attrs['href'])
    company_name.append(company_names[i].text)
    location_name.append(location_names[i].text)
    skills.append(job_skills[i].text)
    

with open('/Users/fahad/Documents/job.csv','w') as file: 
    writer = csv.writer(file)
    writer.writerow(['Job Title','Company Name','Location','Skills','Link'])
    writer.writerows(zip_longest(job_title,company_name,location_name,skills,links))
