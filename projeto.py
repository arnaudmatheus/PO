from __future__ import print_function
from ortools.linear_solver import pywraplp
import numpy as np


arquivo = open("instancia/teste1.txt","r")

qtdTipoUsina = arquivo.readline() #tipos de usina
i = 0 #variavel contadora
fabricas = [] #lista que vai ter as quantidades de fabricas,sendo o indice como guia

for linha in arquivo:
    if(i < int(qtdTipoUsina)):
        tem = linha.split()
        fabricas.append(tem[1])
    if(i+1>=int(qtdTipoUsina)):
        break
    
    i = i + 1

print(fabricas)

i = 0 #variavel contadora
custo = [] #lista com os custos de ligação
for linha in arquivo:
    if(i < int(qtdTipoUsina)):
        tem = linha.split()
        custo.append(tem[1])
    if(i+1>=int(qtdTipoUsina)):
        break
    i = i + 1

i = 0
prodMin = [] #produção minima
for linha in arquivo:
    if(i < int(qtdTipoUsina)):
        tem = linha.split()
        prodMin.append(tem[1])
    if(i+1>=int(qtdTipoUsina)):
        break
    i = i + 1

print(prodMin)


i = 0
prodMax = [] #lista com a produção maxima
for linha in arquivo:
    if(i < int(qtdTipoUsina)):
        tem = linha.split()
        prodMax.append(tem[1])
    if(i+1>=int(qtdTipoUsina)):
        break
    i = i + 1

print(prodMax)

i = 0
custoMin = [] #lista com os custos para produzir o minimo
for linha in arquivo:
    if(i < int(qtdTipoUsina)):
        tem = linha.split()
        custoMin.append(tem[1])
    if(i+1>=int(qtdTipoUsina)):
        break
    i = i + 1

print(custoMin)


i = 0
custoAdd = [] #lista com os custos adicional para produzir acima do minimo
for linha in arquivo:
    if(i < int(qtdTipoUsina)):
        tem = linha.split()
        custoAdd.append(tem[1])
    if(i+1>=int(qtdTipoUsina)):
        break
    i = i + 1

print(custoAdd)

periodos = arquivo.readline() #quantidade de periodos
tempInicio = [] # lista com o horario de inicio do periodo
tempFim = [] # lista com o horario de fim do periodo
demanda = [] # lista com a demanda do periodo

for linha in arquivo:
    tem = linha.split()
    tempInicio.append(tem[0])
    tempFim.append(tem[1])
    demanda.append(tem[2])



