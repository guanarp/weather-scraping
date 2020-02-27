"""
Escrapear(extraer) el dato de la temperatura, la velocidad del viento y direccion de alguna ciudad de interes, 
y luego imprimir esos datos con el día al que corresponde. Se puede elegir cualquier página para hacer esto.
"""
import requests
from bs4 import BeautifulSoup #librerias a usar

page = requests.get("https://www.meteored.com.py/tiempo-en_Asuncion-America+Sur-Paraguay-Central--1-22742.html") #Request pagina de clima de asuncion
soup = BeautifulSoup(page.content, "html.parser") #soup
maxi = soup.find_all("span", class_="maxima changeUnitT") #Se hallan todas las maximas
mini = soup.find_all("span", class_="minima changeUnitT") #las minimas
vel = soup.find_all("span", class_="velocidad") #La velocidad de viento (el rango)
ciudad = soup.find_all("h1", class_="titulo") #La ciudad que se esta analizando

ciudadtex = ciudad[0].get_text()[10:]
"""
Aca se dio un ejemplo del dia actual, mostrando que se imprimia correctamente el primer dato de las listas generadas
maxitex = maxi[0].get_text() 
minitex = mini[0].get_text()
veltex = vel[0].get_text()

print(ciudadtex , "", maxitex, "-", minitex , "", veltex,"\n")
"""

#imrpimiendo las predicciones con sus dias
from datetime import datetime,date
dias = ["Sunday", "Monday", "Tuesday" , "Wednesday", "Thursday", "Friday", "Saturday"] #lista con nombre de los dias
hoy = datetime.today().strftime("%A") #se formatea el dia de hoy en forma de cadena

def impresion(maxima,minima,velocidad,ciudad): #se define una funcion que imprima la maxima, la minima, la velocidad del
#viento para una ciudad dada
    contador = 0 #se usa para iniciar el conteo de dias
    for item in range (0,len(vel)): #se podria usar cualquiera de los otros 2 args en realidad para definir el tamanho de la lista (la ciudad no)
        if contador == 0: #preguntamos por el dia de hoy
            index = dias.index(hoy)#saco el indice para tener que dia de la semana es
        #se imrpime    
        print("Ciudad:",ciudad," dia:",dias[index] ," Temp: ",maxima[item].get_text(),"-",minima[item].get_text()," Velocidad: ",velocidad[item].get_text())
        contador+=1 #para que no inicie de nuevo en hoy cuando vuelva al ciclo
        index+=1 #avanza al sgte dia
        if index == len(dias):
            index = 0 #cuando llega al ultimo dia vuelve a comenzar 
impresion(maxi, mini, vel, ciudadtex)    
        