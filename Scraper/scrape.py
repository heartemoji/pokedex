import requests
from bs4 import BeautifulSoup
import re
import os

# Constants
BASE_URL = "https://bulbapedia.bulbagarden.net"
INDEX_URL = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
INDEX_PAGE = BeautifulSoup(requests.get(INDEX_URL).content, "html.parser")
REGION_TABLES = INDEX_PAGE.find_all('table', attrs={"style" : "border-radius: 10px; -moz-border-radius: 10px; -webkit-border-radius: 10px; -khtml-border-radius: 10px; -icab-border-radius: 10px; -o-border-radius: 10px;; border: 2px solid #FF1111; background: #FF1111;"})

# Region Index Constants
KANTO = 0

def get_pokemon_link(poke_number: int, region: int) -> str:
    """
        Given a pokemons pokedex number, fetch the link to their page from the index
    """
    # create the index string to search with
    padded_index = "#" + str(poke_number).zfill(3) 

    # Search all td's until the padded index is found. Limit to 1 so we don't continue through the whole doc
    # Get the immediate parent of the index td, since the td itself is useless
    poke_row = REGION_TABLES[region].find_all(name="td", limit=1, text=re.compile("\s*" + padded_index + "\n"))[0].find_parent()

    return BASE_URL + poke_row.find("a").get("href")          

def scrape_pokemon(poke_link: str):
    """
        Given a link to the pokemons wiki page, return a dictionary full of values specified
    """

    page_html = BeautifulSoup(requests.get(poke_link).content, features="html.parser")

    poke_table_style="float:right; text-align:center; width:33%; max-width:420px; background: #78C850; border: 2px solid #682A68; padding:2px;"
    poke_table = page_html.find("table", attrs={"style" : poke_table_style})
    top_section = poke_table.find("table", attrs={"style": "background:#A7DB8D; padding:2px; border-spacing:3px;"})

    # Extract name, class, and number
    poke_name = top_section.find(name="big").text
    poke_class = top_section.find(title="Pokémon category").text
    poke_number = top_section.find("a", title="List of Pokémon by National Pokédex number").text
    
    # Download image
    poke_pic_link = "http://" + top_section.find("img")["src"][2:]
    image_response = requests.get(poke_pic_link, stream=True)
    
    img_filename = poke_name + ".png"
    with open(img_filename, "wb") as file:
        file.write(image_response.content)

    # Extrat Type(s)
    type_table = poke_table.find("a", href="/wiki/Type").find_parent("b").find_next_sibling("table")

    # Filter function, to ignore random "Unknown" hidden types in this table
    def type_filter(tag):
        if tag.find("b") != None:
            if tag.find("b").text == "Unknown":
                return False
            else:
                return True
        return False 

    types = type_table.find_all(type_filter)
    valid_types = set([])
    for tag in types:
        valid_types.add(tag.find("b").text)
    

    # Extract height, first in imperial and then metric
    height_pair = poke_table.find("a", title="List of Pokémon by height").find_parent("b").find_next_sibling("table").find_all("td", limit=2)
    heights = []
    for td in height_pair:
        heights.append(td.text.strip())
        

    return {"name" : poke_name, "number": poke_number, "class" : poke_class, "image_path": os.path.join(os.path.dirname(__file__), img_filename), "height" : heights }


def main():
    return None

if __name__ == "__main__":
    # main()
    bulbasaur = scrape_pokemon("https://bulbapedia.bulbagarden.net/wiki/Bulbasaur_(Pok%C3%A9mon)")
    print(bulbasaur)
