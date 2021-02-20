import requests
from bs4 import BeautifulSoup
import re

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
        Given
    """
    return None


def main():
    return None

if __name__ == "__main__":
    main()
