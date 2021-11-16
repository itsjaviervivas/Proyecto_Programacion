#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 18:37:13 2021

@author: javiervivas
"""

import regresion1 as r1

data = r1.pregunta()
header = r1.header(data)
datay = r1.extraey(data, header)
variable = r1.extraerdatos(data, header)
exp = r1.extraedatos2(data, header, variable)
Matrix = r1.matrizmarkov(exp, variable)
y = r1.regresionlineal(Matrix, datay)
r2 = r1.rsquared(y, datay, data)

