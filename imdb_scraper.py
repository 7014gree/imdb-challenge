import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.imdb.com/title/tt0110912/?ref_=nv_sr_srsg_0")
html_string = r.text
print(html_string)