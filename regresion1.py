#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 18:36:26 2021

@author: javiervivas
"""

import pandas as pd
import numpy as np
import matplotlib as plt

#revisar si es posible dejarla a un lado
def pregunta():
    database = input("Nombre de la base de datos (Incluya el '.csv'): ") #pregunta el nombre de la base
    delimitar = input("Formato en la que está delimitado (',', ';', etc): ")
    data = pd.read_csv(database, delimiter= delimitar)
    cuantanas = data.isnull().sum().sum()
    print ('Cantidad de NaN (O variables vacias): ', cuantanas)
    data = data.fillna(0) #para arreglar los nans, reemplaza por 0
    return data

def header(data):
    header = data.columns
    print(header)
    return data

def extraey (data, header):
    daty = []
    variabledep = input("¿Cuál es la variable dependiente que tiene el modelo?: ")
    daty.append(data[[variabledep]])
    datay = np.array(daty) 
    print(datay)
    return datay
    
def extraerdatos (data, header):
    """Vamos a estimar las Betas de la regresión lineal, mediante el método de minimos cuadrados."""
    variable = int(input("¿Cuántas variables explicativas tiene el modelo?: "))
    return variable
def extraedatos2 (data, header, variable):
    #extrae los datos de la base de datos
    vari = []
    exp = []
    for i in range(variable):
        variablex = input("¿Cuáles son variables explicativas tiene el modelo?: ")
        if variablex in header:
            vari.append(variablex)
            exp.append(data[variablex])
        else:
            print("No existe.")

    print(exp)
    return exp

def matrizmarkov(exp, variable):
    # Crea una matriz vacia
    j, r = variable+1, len(exp[1])
    Matrix = [[0 for x in range(j)] for y in range(r)] 
    print(Matrix)
    #crear el vector de unos y los añade 
        for i in range(len(exp[1])):
            Matrix[i][0]= 1
    n=0
    for i in range(variable):
        for i in range(len(exp[1])):
            Matrix[i][0+n] = exp[0+n[i]
        n+=1
    return Matrix


def regresionlineal(Matrix, datay):
    #convierte esa matriz en un array comun y corriente
    A = np.array(Matrix)
    A

    #halla la transpuesta de esa matriz
    At = np.transpose(A)
    At

    #Multiplica a A con At
    AAt = np.dot(A,At)
    AAt  

    #halla la inversa de la matriz

    Ai = np.linalg.inv(AAt)
    Ai

    #Multiplicamos nuevamente Ai con At
    y1 = np.dot(Ai, At)

    #finalmente, la regresion sería
    y = np.dot(y1, datay)
    return y

def estimacionErrores(datay, y):
    #los errores del modelo
    u = np.subtract(datay, y) 
    return u
    
def rsquared (datax, datay, df):
    """Va a hallar el R^2. Recibe la variable dependiente y las independientes."""
    #En si r^2 lo podemos definir como R^2= 1-SSR/SST
    df = len(datay)-len(datax)-1 # los grados de libertad
    yhat = np.p(datax)                         #lo usaremos para que nos haga el fit
    ybar = np.sum(datay)/len(datay)  #metodo provisonal, mirar que tal funciona
    ssr = np.sum((yhat-ybar)**2)   # a ssr lo podemos definir como la sumatoria de errores al cuadrado
    sst = np.sum((datay-ybar)**2)     # a sst lo podemos definir como sse + ssr
    r2 = 1 - (ssr /sst)
    adr2 = 1-(1-r2)*(len(datay-1))/(df) #el r^2 ajustado
    return r2, adr2 #revisar muy bien que esto tenga sentido alguno

#Opcion 4 del set (Revisar opciones para graficar regresiones linelaes)
def graficar(y):
    #grafica:
    grafica = plt.plot(y)
    plt.show()
