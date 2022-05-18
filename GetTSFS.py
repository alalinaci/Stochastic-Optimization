import openpyxl
import pandas as pd

# Loading excel sheet
wb = openpyxl.load_workbook(r'''excel petg.xlsx''')
data = wb['Data']


# Defining the variables by reading them from excel sheet
df = pd.read_excel('excel petg.xlsx', sheet_name = 'Data', skiprows = 1)
build_orientation = df['Build Orientation'].unique() #returns a list of unique build orientation parameter from excel sheet
speed = df['Speed'].unique() #returns a list of unique speed parameter from excel sheet
infill_density = df['Infill Density'].unique() #returns a list of unique infill density parameter from excel sheet
temp = df['Temp'].unique() #returns a list of unique temperature parameter from excel sheet
layer_thickness = df['Layer Thickness'].unique() #returns a list of unique layer thickness parameter from excel sheet
tensile_strength_list = []
flexural_strength_list = []
w = 0.5

# Calculating Tensile Strength using regression function
def get_tensile_strength():
    for bo in build_orientation:
        for s in speed:
            for id in infill_density:
                for t in temp:
                    for lt in layer_thickness:
                        TS = - 0.246 + 0.000059 * bo + 0.00144 * s + 0.001327 * id + 0.000891 * t + 0.071  * lt
                        tensile_strength_list.append(TS)

# Calculating Flexural Strength using regression function
def get_flexural_strength():
    for bo in build_orientation:
        for s in speed:
            for id in infill_density:
                for t in temp:
                    for lt in layer_thickness:
                        FS = 5.49 - 0.00632 * bo - 0.0081 * s + 0.01007 * id - 3.96 * lt + 0.00085 * t
                        tensile_strength_list.append(FS)