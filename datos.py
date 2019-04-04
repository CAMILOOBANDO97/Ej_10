import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos8 = pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_2/Fourier/Datos/transacciones2008.txt', sep=";",names=['A','B','C','D'])
datos9 = pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_2/Fourier/Datos/transacciones2009.txt', sep=";",names=['A','B','C','D'])
datos1 = pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_2/Fourier/Datos/transacciones2010.txt', sep=";",names=['A','B','C','D'])

datos8["Fechas"] = datos8["A"].astype(str).str[0:-8] + " " + datos8["B"].str[11:19]
datos9["Fechas"] = datos9["A"].astype(str).str[0:-8] + " " + datos9["B"].str[11:19]
datos1["Fechas"] = datos1["A"].astype(str).str[0:-8] + " " + datos1["B"].str[11:19]

D8=datos8.drop(["A", "B", "D"], axis = 1)
D8["Fechas"]=pd.to_datetime(D8["Fechas"])
newC=[float(dto.replace(",",".")) for dto in D8["C"]]
D8["C"]=newC

plt.scatter(D8["Fechas"],D8["C"])
plt.savefig("preciotiempo")