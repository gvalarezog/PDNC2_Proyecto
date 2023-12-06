import requests
from bs4 import BeautifulSoup
import pandas as pd


nombres = list()
apellidos = list()
cursos = list()
url = 'http://127.0.0.1:8000/'
html_doc = requests.get(url)
print(html_doc)
soup = BeautifulSoup(html_doc.text, 'html.parser')
# data = soup.find_all('td',attrs={"class": "table-primary"})
# i=0
# # print(data)
#
# while(i+2<len(data)):
#     nombres.append(data[i].text)
#     apellidos.append(data[i+1].text)
#     cursos.append(data[i+2].text)
#     i+=3

# for d in data:
#     nombres.append(data[i])
#     apellidos.append(data[i])
#     cursos.append(data[i])
#     i+=1

tabla = soup.find('table')
# print(tabla)
# Obtener las filas de la tabla
filas = tabla.find_all('tr')
# print(filas)
# Iterar sobre las filas e imprimir los datos
for fila in filas:
    # # Obtener las celdas de la fila
    celdas = fila.find_all('td')
    print(celdas)
    if len(celdas)>0:
        nombres.append(celdas[0].string)
        apellidos.append(celdas[1].string)
        cursos.append(celdas[2].string)

print(apellidos)
print(nombres)
print(cursos)

df = pd.DataFrame({'Nombres':nombres,'Apellidos':apellidos,'Cursos':cursos})
df.to_csv('personas.csv', index=False, encoding='utf-8')
# for d in data:
#
#     print(d)
# print(ancor)
# print(soup.prettify())