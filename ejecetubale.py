#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 18:37:13 2021

@author: javiervivas
"""

import regresion1 as r1

print("Este programa le permite realizar una regresión lineal por el método de minimos cuadrados ordinarios, para continuar escriba *continuar* y llene la información necesaria) 
a=input("Ingrese")
if a==continuar:
  data = r1.pregunta()
  header = r1.header(data)
  datay = r1.extraey(data, header)
  variable = r1.extraerdatos(data, header)
  exp = r1.extraedatos2(data, header, variable)
  Matrix = r1.matrizmarkov(exp, variable)
  y = r1.regresionlineal(Matrix, datay)


