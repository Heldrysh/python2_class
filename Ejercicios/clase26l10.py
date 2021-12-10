"""
Clase del 26/10/2021
"""
import pandas as pd

ecoli_matraz = pd.Series([0.1, 0.15, 0.19, 0.5],
                         name='matraz'
                          )
print(ecoli_matraz)

#Especificamos el indice 
ecoli_matraz = pd.Series([0.1, 0.15, 0.19, 0.5,
                         0.9, 1.4, 1.8, 2.1, 2.3],
                         index=['t1', 't2', 't3', 't4',
                                't5', 't6', 't7', 't8', 't9'],
                         name='matraz'
                         )

#realizamos operaciones
ecoli_matraz2 = pd.Series([0.1, 0.15, 0.19, 0.5,
                         0.9, 1.4, 1.8, 2.1, 2.3],
                         name='matraz'
                         )
print(ecoli_matraz2*0.39)

#Hacemos operaciones haciendo uso de indicesXDXD
ODs = pd.Series([0.2, 0.2, 0.4, 0.1, 0.2, 0.1, 0.2, 0.4, 0.1],
                index = [8,4,1,2,3,0,5,7,6],
                name='ajustes')
print(ODs * ecoli_matraz2)

#Ejercicio#1
produccion = pd.Series([5, 11, 4, 7, 2],
                        index = ['gen1', 'gen2', 'gen3', 'gen4', 'gen5'])
costos = pd.Series([ 5, 4.3, 7, 3.5],
                  index =['gen1', 'gen2', 'gen3', 'gen5'])

print(costos/produccion.T)
#NO obtuvimos info pero se proceso

nan_test = pd.Series([0.1, None, 2.1, 2.3],
                         name='matraz')
print(nan_test)
#Pasamos con gran indiferencia de los Nan porque al igual que los recuerdos de nuestros exs no nos sirve pa' na'

class mamifero():
    vertebrado = True
array_test = pd.Series([0.1, 'a', 0.19, mamifero, 2.1],
                         name='multiples objetos'
                         )
print(array_test)

#Acceso
series_test2 = pd.Series([5.1, 2.2, 1.1, 3.1, 4.2],
                         index = [5,2,1,3,4])
print(series_test2)
print(series_test2.iloc[1])
print(series_test2.loc[1])
print(series_test2[1::2])
print(series_test2.loc[1::2])
print(series_test2.iloc[1::2])

#booleanos
 bool_min = costo_unitario == costo_unitario.min()
 bool_max = costo_unitario == costo_unitario.max()

 print(costo_unitario[bool_min | bool_max])