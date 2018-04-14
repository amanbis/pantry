# Hey ya'll I am importing the parsing library
import urllib.request
from bs4 import BeautifulSoup
url = "https://www.epicurious.com/recipes/food/views/three-bean-soup"
res = urllib.request.urlopen(url)
html = res.read()
bs = BeautifulSoup(html, "html.parser")
recipe = bs.find_all(lambda tag: tag.name == 'li' and 
                                   tag.get('class') == ['ingredient'])