from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("https://www.lusakatimes.com/")
soup = BeautifulSoup(page_to_scrape.text,"html.parser")
headlines = soup.findAll("h3", attrs={"class":"entry-title td-module-title"})


file = open(r"C:\Users\Humphrey\Documents\SCHOOL\PERSONAL\Phython\code\csv\Headlines.csv",'w')
csv_writer = csv.writer(file) 

csv_writer.writerow("Headlines")

for headline in headlines:
    csv_writer.writerow([headline.text])
file.close()


