import requests
from bs4 import BeautifulSoup

film_request = requests.get("https://www.imdb.com/title/tt0110912/?ref_=nv_sr_srsg_0")
film_html_string = film_request.text
film_soup = BeautifulSoup(film_html_string, 'html.parser')

# Writes html string to text.txt for easy review.
def write_to_txt(string):
    with open('text.txt', 'w', encoding="utf-8") as f:
            f.write(string)
    print("Written successfully")

all_actors_html = film_soup.findAll(name = 'a', attrs={'class': "sc-bfec09a1-1 gfeYgX"})
actors_list = []
for actor_html in all_actors_html:
    actor_dictionary = dict()
    actor_name = actor_html.txt
    actor_url = "https://www.imdb.com/" + actor_html['href']
    print(actor_url)
    movies_list = []
    
    # print(actor_dictionary)

    actor_request = requests.get(actor_url)
    actor_html_string = actor_request.text
    actor_soup = BeautifulSoup(actor_html_string, 'html.parser')
    all_movies_div = actor_soup.find(name = 'div', attrs={'class': "filmo-category-section"})
    movie_divs = all_movies_div.findAll(name = 'div')
    for movie_div_html in movie_divs:
        try:
        #write_to_txt(movie_div_html.prettify())
            """
            Can find year and movie like this:
                movie_html_children = movie_html.findChildren()
                year = movie_html_children[0].text.strip()
                movie = movie_html_children[1].find(name = 'a').text

            Alternatively find movie like this:
                movie_b = movie_html.find(name = 'b')
                movie = movie_b.find(name = 'a').text
            """

        
            year_html = movie_div_html.find(name = 'span')
            year = year_html.text.strip()

            movie_title_html_b = year_html.find_next_sibling()#movie_html.find(name = 'b')
            movie_title_html_a = movie_title_html_b.find(name = 'a')
            movie_title = movie_title_html_a.text
            
            movies_list.append({'title': movie_title, 'year': year})
        except:
            pass

    actor_dictionary.update({'name': actor_html.text, 'link': actor_url, 'movies': movies_list})

    actors_list.append(actor_dictionary)

write_to_txt(f"{actors_list}")
