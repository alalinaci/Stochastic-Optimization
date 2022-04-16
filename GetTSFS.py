# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 01:19:06 2022

@author: alalinaci

This script finds full factorial TS and FS

"""
# Imports
import openpyxl
import pandas as pd

# Loading excel sheet
wb = openpyxl.load_workbook(r'''DATA_PSO_BFO.xlsx''')
ws = wb['PETG']


# Defining the variables by reading them from excel sheet
df = pd.read_excel('DATA_PSO_BFO.xlsx', sheet_name = 'PETG', skiprows = 1)
layer_thickness = df['Layer Thickness (mm)'].unique() #returns a list of unique layer thickness parameter from excel sheet
feed_rate = df['Feed Rate (mm/s)'].unique() #returns a list of unique feed rate parameter from excel sheet
infill_density = df['Infill Density (%)'].unique() #returns a list of unique infill density parameter from excel sheet
tensile_strength_list = []
flexural_strength_list = []
w = 0.5

# Calculating Tensile Strength using regression function
def get_tensile_strength():
    for L in layer_thickness:
        for S in feed_rate:
            for D in infill_density:
                TS = 27.59 - 29.71 * L  - 0.0798 * S + 0.0948 * D
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
                FS = 93.87 - 52.2 * L - 0.1854 * S - 0.0752 * D
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
    wb.close()