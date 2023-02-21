# Bismillah
import requests as re
from bs4 import BeautifulSoup as beu


response = re.get("https://www.verywellmind.com/what-is-morality-5076160")


soup = beu(response.text, "html.parser")
la = soup.select("#wellness-sc-page_1-0 ")
for i in la:
    print(i.get_text())


with open('note.txt', 'a') as file:
    file.write(i.get_text())
