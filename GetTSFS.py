# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 01:19:06 2022

@author: Gayatri Dhankhar

This script finds full factorial TS and FS

"""
# Imports
import openpyxl

# Loading excel sheet
wb = openpyxl.load_workbook(r'''DATA_PSO_BFO.xlsx''')
ws = wb['PETG']


# Defining the variables
layer_thickness = [0.17, 0.23, 0.3]
feed_rate = [30, 40, 50]
infill_density = [60, 70, 80]
tensile_strength_list = []
flexural_strength_list = []
w = 0.5

# Calculating Tensile Strength using regression function
def get_tensile_strength():
    for L in layer_thickness:
        for S in feed_rate:
            for D in infill_density:
                TS = 24.100+1.586*L+0.647*L-2.234*L+1.292*S-0.987*S-0.305*S-0.871*D-0.153*D+1.024*D
                tensile_strength_list.append(TS)
                #print("Tensile Strength: ", TS, " Layer Thickness: ", L, " Feed Rate: ", S, " Infill Density: ", D)
    for i, tensile_strength in enumerate(tensile_strength_list):
        ws.cell(row=i+3, column=6).value = tensile_strength
    wb.save('DATA_PSO_BFO.xlsx')


# Calculating Flexural Strength using regression function
def get_flexural_strength():
    for L in layer_thickness:
        for S in feed_rate:
            for D in infill_density:
                FS = 69.007+3.249*L+0.281*L-3.530*L+1.145*S+1.418*S-2.562*S+1.502*D-1.501*D-0.001*D
                flexural_strength_list.append(FS)
                #print("Flexural Strength: ", FS, " Layer Thickness: ", L, " Feed Rate: ", S, " Infill Density: ", D)
    for i, flexural_strength in enumerate(flexural_strength_list):
        ws.cell(row=i+3, column=8).value = flexural_strength
    wb.save('DATA_PSO_BFO.xlsx')


# Calculating Fitness Value for each specimen
def get_fitness_value():
    Z = [w*tensile_strength_list[i]+w*flexural_strength_list[i] for i in range(len(tensile_strength_list))]
    for j, fitness_value in enumerate(Z):
        ws.cell(row=j+3, column=9).value = fitness_value
    wb.save('DATA_PSO_BFO.xlsx')