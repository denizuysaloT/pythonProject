from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import os

if not os.path.exists('downloaded_files'):
    os.makedirs('downloaded_files')

# Sayfa URL'sini ayarlayın
url = 'url'

# GET isteği gönderin ve sayfanın kaynak kodunu indirin
response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')

#class yazın

for element in soup.find_all(class_="class"):
    element.extract()


for tag in soup.find_all():
    if tag.has_attr('href') and tag['href'] != 'javascript:void(0)':
        file_url = urljoin(url, tag['href'])
    elif tag.has_attr('src') and tag['src'] != 'javascript:void(0)':
        file_url = urljoin(url, tag['src'])
    else:
        continue

    filename = os.path.join('downloaded_files', os.path.basename(file_url))

    file_response = requests.get(file_url)
    with open(filename, 'wb') as f:
        f.write(file_response.content)

filename = os.path.join('downloaded_files', 'index.html')
with open(filename, 'w') as f:
    f.write(str(soup))
