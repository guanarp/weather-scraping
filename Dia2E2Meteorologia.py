"""
recolectaremos de una pagina que da la temperatura de asuncion de una pagina del clima
datos a usar:
https://www.meteored.com.py/tiempo-en_Asuncion-America+Sur-Paraguay-Central--1-22742.html
class="dato-temperatura changeUnitT
"""
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.meteored.com.py/tiempo-en_Asuncion-America+Sur-Paraguay-Central--1-22742.html")
soup = BeautifulSoup(page.content, "html.parser")
temp = soup.find_all("span", class_="dato-temperatura changeUnitT")
"""
primeramente debemos de inspeccionar la pagina y el elemento que necesitamos extraer sus datos y  debemos identificar con que 
atributos podemos extraer esos datos
"""
temptex = temp[0].get_text()
print(temptex)