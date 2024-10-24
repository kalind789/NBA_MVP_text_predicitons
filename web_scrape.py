import requests
from bs4 import BeautifulSoup
import re
import torch
from transformers import BertTokenizer, BertForSequenceClassification

url = 'https://bleacherreport.com/articles/10136625-ranking-5-potential-first-time-nba-mvp-candidates'
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    print(html_content[:500])
else:
    print("Failed to load url")

soup = BeautifulSoup(html_content, 'html.parser')

data = {
    "paragraphs": [],
    "headlines": []
}

# Store paragraphs
paragraphs = soup.find_all('p')
for _, paragraph in enumerate(paragraphs):
    data["paragraphs"].append(paragraph.text)

# Store headlines
headlines = soup.find_all('h2')
for _, headline in enumerate(headlines):
    data["headlines"].append(headline.text)

# Removing white space from the paragraphs
cleaned_paragraphs = [re.sub('\s+', ' ', para.strip()) for para in data['paragraphs']]
cleaned_headlines = [re.sub('\s+', ' ', headline.strip()) for headline in data['headlines']]

print("Headlines Overview:")
for i, headline in enumerate(cleaned_headlines):
    print(f"{i+1}. {headline}")

print("\nContent Summary:")
for i, para in enumerate(cleaned_paragraphs):
    print(f"Paragraph {i+1}: {para}")