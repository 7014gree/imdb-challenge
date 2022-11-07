import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.imdb.com/title/tt0110912/?ref_=nv_sr_srsg_0")
html_string = r.text
soup = BeautifulSoup(html_string, 'html.parser')

# Writes html string to text.txt for easy review.
def read_to_txt(_soup):
    with open('text.txt', 'w', encoding="utf-8") as f:
            f.write(_soup.prettify())
    print("Written successfully")

actors_html = soup.findAll(name = 'a', attrs={'class': 'sc-bfec09a1-1 gfeYgX'})
actors_dictionary = dict()
for tag in actors_html:
    actors_dictionary.update({'name': tag.text, 'link': "https://www.imdb.com/" + tag['href'], 'movies': []})

for actor_url in actors_dictionary.values():
    r = requests.get(actor_url)
    html_string = r.text
    soup = BeautifulSoup(html_string, 'html.parser')
    read_to_txt(soup)
    break
