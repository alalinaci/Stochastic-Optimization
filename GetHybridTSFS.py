import openpyxl

tensile_strength_list = []
flexural_strength_list = []
def get_tensile_flexural_strength():
    layer_thickness = [0.17, 0.23, 0.3]
    feed_rate = [30, 40, 50]
    infill_density = [60, 70, 80]
    for L in layer_thickness:
        for S in feed_rate:
            for D in infill_density:
                tensile_strength = 27.59 - 29.71 * L  - 0.0798 * S + 0.0948 * D
                tensile_strength_list.append(tensile_strength)
                flexural_strength = 93.20 - 52.2 * L - 0.1854 * S - 0.0752 * D
                flexural_strength_list.append(flexural_strength)
    #print (tensile_strength_list)
    #print(flexural_strength_list)

# Calculating Fitness Value for each specimen
def get_fitness_value():
    wb = openpyxl.load_workbook(r'''DATA_PSO_BFO.xlsx''')
    ws = wb['PETG']
    w=0.5
    Z = [w*tensile_strength_list[i]+w*flexural_strength_list[i] for i in range(len(tensile_strength_list))]
    for j, fitness_value in enumerate(Z):
        ws.cell(row=j+3, column=11).value = fitness_value
    wb.save('DATA_PSO_BFO.xlsx')
    wb.close()