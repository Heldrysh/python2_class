"""
Clase de biopython 09/11/2021
uso de numpy y pandas tambien para costos y la graficacion con matplot 
no hay dudad
"""
import pandas as pd
import numpy as np
#primer dataFRame 
pd_DF = pd.DataFrame(np.random.rand(3, 2),
                     columns=["columna_1", "columna_2"],
                     index=['a','b','c'])

produccion = pd.Series([5, 11, 4, 7, 2],
                       index= ['gen1', 'gen2', 'gen3','gen4', 'gen5'],
                       name='production')
costos = pd.Series([ 5, 4.3, 7, 3.5],
                  index=['gen1', 'gen2', 'gen3', 'gen5'],
                  name='costos')
#generamos un dataframe de salida estas cosas son geniales les cabe de todo
costo_benecio = pd.DataFrame({'costos':costos,
                              'produccion':produccion})

produccion = pd.Series([5, 11, 4, 7, 2],
                        index=['gen1', 'gen2', 'gen3', 'gen4', 'gen5'],
                        name='produccion')
costos = pd.Series([ 3.5, 5, 7, 4.3],
                  index=['gen1', 'gen2', 'gen3', 'gen5'],
                  name='costos')
costo_beneficio = pd.DataFrame({'costos': costos,
                       'produccion': produccion})

#Ejercicio#2
produccion_30 = pd.Series([5, 11, 4, 7, 2],
                        index=['gen1', 'gen2', 'gen3', 'gen4', 'gen5'],
                        name='produccion')
produccion_35 = pd.Series([3, 7, 9, 4, 6],
                        index=['gen1', 'gen2', 'gen3', 'gen4', 'gen5'],
                        name='produccion')
costos = pd.Series([ 3.5, 5, 7, 4.3],
                  index=['gen1', 'gen2', 'gen3', 'gen5'],
                  name='costos')
costo_beneficio = pd.DataFrame({'costos': costos,
                       'produccion 30°': produccion_30,
                        'produccion 35°': produccion_35})

#Se obtiene el costo unitario 
columnas_interes = ['produccion 30°', 'produccion 35°']
producciones = costo_beneficio.loc[:, columnas_interes]
costos_unitarios = producciones.div(costo_beneficio.costos, axis=0)
costos_unitarios.rename( columns = {'produccion 30°':'costo unitario 30°', #REalizamos un Rename
                                   'produccion 35°':'costo unitario 35°'},
                         inplace=True)

###DIVISIONXDXDXDXD#####
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

#Generacion de la figura
fig = plt.figure()
ax = plt.axes() #creamos el eje x
x = np.linspace(0, 10, 1000) #especificamos 
#Plot de X y Y
ax.plot(x, np.sin(x))

ax.set(xlim=(0, 10), ylim=(-2, 2),  #limites
       xlabel="x", ylabel="sen(x)", #tags
       title="grafiquita")       #titulo
plt.show()

#generamos 2 subPlots a 1 y 2
fig, axs = plt.subplots(nrows = 1, ncols = 2)

axs[0].plot(x, np.sin(x))

axs[1].plot(x, np.cos(x)) 

plt.show() #se muestra el plt