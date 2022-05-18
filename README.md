## Stochastic Optimization
### Particle Swarm Optimization
#### Objective: Optimizing PETG FDA Tensile and Flexural Strength Using Linear Regression Analysis Equation
![Demo](https://github.com/alalinaci/Stochastic-Optimization)
#### Pre-requisites: 
* An excel worksheet containing layer thickness, feed rate and infill density parameters
* The excel sheet must be in the same directory as `PSO.py` and `GetTSFS.py`
* Compatible with Microsoft Excel 16.x.x onwards
* Python dependencies are listed in `requirements.txt`
#### Algorithm:
*GetTSFS.py*
* Load excel sheet and workbook as: 
```
wb = openpyxl.load_workbook(r'''DATA_PSO_BFO.xlsx''')
ws = wb['PETG']
```
* Fetch varibles from excel sheet
* Calculate Tensile Strength for each specimen using Linear Regression Analysis Equation as:
```
TS = 24.100+1.586*L+0.647*L-2.234*L+1.292*S-0.987*S-0.305*S-0.871*D-0.153*D+1.024*D
```
* Calculate Flexural Strength for each specimen using Linear Regression Analysis Equation as:
```
FS = 69.007+3.249*L+0.281*L-3.530*L+1.145*S+1.418*S-2.562*S+1.502*D-1.501*D-0.001*D
```
* Calculate Fitness Value for each specimen using Weighted Sum Equation (weight of TS = weight of FS = 0.5) as:
```
Z = [w*tensile_strength_list[i]+w*flexural_strength_list[i] for i in range(len(tensile_strength_list))]
```
* Populate and save the data in excel sheet

*PSO.py*
* import and execute `get_flexural_strength()`, `get_tensile_strength()` and `get_fitness_value()` function from `GetTSFS.py`
* Read data from excel to calculate `TSmax` and `FSmax`
* Finally, plug the values into final objective function to get the combined fitness value of Tensile Strength and Flexural Strength as:
```
def objective_function(X): 
    Zmax = w*TSmax+w*FSmax
    return Zmax
```
* Other parameters will be set as under:
```
bounds=[(19,28),(61,72)] # upper and lower bounds of variables (TS and FS) obtained through experiment, needs to be fed manually
nv = 2                   # number of variables is taken as one, as we only intend to maximize tensile strength
mm = 1                   # since we're maximizing tensile strength, for min mm=-1
  
# THE FOLLOWING PARAMETERS ARE OPTIONAL.
particle_size=50         # number of particles
iterations=100           # max number of iterations                    # inertia constant is set to 0.5 for both TS and FS
c1=2                     # cognative constant
c2=2   
```
* `objective_function()` returns the final optimal fitness value with a combined effect of Tensile Strength and Flexural Strength using PSO
* This fitness value will be compared with BFO and hybrid methods to determine the accuracy of the three algorithms deployed
* Command Line Outputs have been removed and all the values are taken from and written into the excel file to enhance readability

#### Steps to Execute PSO:
1. Clone the repository as `git clone https://github.com/alalinaci/Stochastic-Optimization.git` (if you have git setup already, else download the files as zip and extract)
2. Make sure that the excel file is closed before executing any python script, as values can't be written into an open excel file and the script will throw "Permission" error
3. Run `PSO.py`
4. Check the results in excel file under PSO BFO Hybrid worksheet 

#### Steps to Execute BFO:
1. Clone the repository as `git clone https://github.com/alalinaci/Stochastic-Optimization.git` (if you have git setup already, else download the files as zip and extract)
2. Make sure that the excel file is closed before executing any python script, as values can't be written into an open excel file and the script will throw "Permission" error
3. Run `BFO.py`
4. Check the results in excel file under PSO BFO Hybrid worksheet 

#### Steps to Execute PSO-BFO Hybrid:
1. Clone the repository as `git clone https://github.com/alalinaci/Stochastic-Optimization.git` (if you have git setup already, else download the files as zip and extract)
2. Make sure that the excel file is closed before executing any python script, as values can't be written into an open excel file and the script will throw "Permission" error
3. Run `Hybrid.py`
4. Check the results in excel file under PSO BFO Hybrid worksheet 

#### Steps to Display Graphs:
1. Clone the repository as `git clone https://github.com/alalinaci/Stochastic-Optimization.git` (if you have git setup already, else download the files as zip and extract)
2. Make sure that the excel file is closed before executing any python script, as values can't be written into an open excel file and the script will throw "Permission" error
3. Run `Graphs.py`
4. Check the results in excel file under PSO BFO Hybrid worksheet 

***Note:*** *Please execute PSO first, followed by BFO, then Hybrid*
