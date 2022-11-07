import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.imdb.com/title/tt0110912/?ref_=nv_sr_srsg_0")
html_string = r.text
soup = BeautifulSoup(html_string, 'html.parser')

with open('text.txt', 'w', encoding="utf-8") as f:
        f.write(soup.prettify())