import csv

import requests
import time
from bs4 import BeautifulSoup

url = "https://developer.infermedica.com/docs/available-symptoms"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html5lib')

# Removing the inline span tag and related text from "soup"
for span_tag in soup.find_all('span', class_="hint"):
    span_tag.replace_with('')

symptom_all = soup.find_all('li', class_="list__item alphabet__list-item")

f = open('infermedica_symptoms.csv', 'w')
w = csv.writer(f)
for symptom in symptom_all:
    # symptom.text.split(',')
    w.writerow(symptom.text.split(','))
f.close()
