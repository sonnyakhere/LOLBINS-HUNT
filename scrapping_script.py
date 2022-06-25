from csv import writer
from bs4 import BeautifulSoup
import requests

url = "https://lolbas-project.github.io/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('tr')

with open('lolbas.csv', 'w', encoding='utf8', newline='') as l:
    thewriter = writer(l)
    header = ['Binaries']
    thewriter.writerow(header)

    for list in lists[1:-1]:
        binary = list.find('a', class_="bin-name")
        if binary is not None:
            info = [binary.text]
        else:
            info = None

        thewriter.writerow(info)

    

    
