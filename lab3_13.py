import matplotlib.pyplot as plt         # библиотека для графиков
import pandas as pd                     # библиотека для обработки табличных данных
import math                             # библиотека для математики
import numpy as np


def deviation_count(list1):
  average = sum(list1) / len(list1)
  deflection_squared = []
  for val in list1:
    deflection_squared.append((val - average) ** 2)
  t = 1.1
  return average, t * np.sqrt(sum(deflection_squared) / (len(list1) * (len(list1) - 1)))

cols=[1,2,3,4]
data = pd.read_excel('lab13.xlsx', sheet_name = 'Lab13', usecols = cols)
data.head()
Rotation_Step = 10

val0= data['ein'].tolist()
val0 = list(map(float, val0))
val10= data['zwei'].tolist()
val10 = list(map(float, val10))
val20= data['drei'].tolist()
val20 = list(map(float, val20))
val30= data['vier'].tolist()
val30 = list(map(float, val30))
Difference = []


for val in range (len(val0)):
  Difference.append(abs(val10[val]-val0[val]))
  Difference.append(abs(val20[val]-val10[val]))
  Difference.append(abs(val30[val] - val20[val]))


Difference = [(2*x)/(10*Rotation_Step) for x in Difference]

sss, DeltaDiff = deviation_count(Difference)
Wavelength = 1000000 * np.average(Difference)
DeltaDiff = 1000000*DeltaDiff
cols=[0,1,2]
data = pd.read_excel('длины волн.xlsx', sheet_name = 'colors', usecols = cols)
data.head()
minlen= data['min'].tolist()
minlen = list(map(int,minlen ))
maxlen= data['max'].tolist()
maxlen = list(map(float, maxlen))
color= data['color'].tolist()


print("Длина волны света равна\n", f"{Wavelength:.1f} \u00B1 {DeltaDiff:.1f} нм")

print("Это соответствует ", end="")
for val in range(len(minlen)):
  if Wavelength > minlen[val] and Wavelength < maxlen[val]:
    print(color[val], "свету")


cols=[0,1,2,3,4]
data = pd.read_excel('lab13.xlsx', sheet_name = 'Yung', usecols = cols)
data.head()
L = 0.36
slit1= data['first'].tolist()
slit1 = list(map(float, slit1))
slit2= data['second'].tolist()
slit2 = list(map(float, slit2))
slit3= data['third'].tolist()
slit3 = list(map(float, slit3))
slit4= data['fourth'].tolist()
slit4 = list(map(float, slit4))

h = []

def Yung(slit):
  psi = []
  for val in range(2, len(slit)):
    psi.append(slit[val]*10**-3/L)
    h.append(Wavelength*10**-9/psi[val-2])


Yung(slit1)
Yung(slit2)
Yung(slit3)
Yung(slit4)

h_av, delta_h  = deviation_count(h)


print("\nШирина когерентности равна")
print(f"{h_av*10**3:.2f}\u00B1{delta_h*10**3:.2f} mm")







