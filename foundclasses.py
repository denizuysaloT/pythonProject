import requests
from bs4 import BeautifulSoup
url = "url"
response = requests.get(url)
if response.status_code != 200:
    print("Sayfa yüklenirken bir hata oluştu.")
else:
    soup = BeautifulSoup(response.content, "html.parser")

    classes = set()
    for element in soup.find_all(True):
        if element.has_attr('class'):
            for class_name in element['class']:
                classes.add(class_name)

    if not classes:
        print("Sayfada sınıf öğesi yok.")
    else:
        print("Sayfadaki sınıflar:")
        for class_name in classes:
            print(class_name)
