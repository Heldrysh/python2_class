"""
NAME
       Numpy.py
VERSION
        1.0
AUTHOR
        Diego Montes Gabriel <<dmontes@lcg.unam.mx>>
DESCRIPTION 
        Imprimimos los arrays de manera estructurada de los arrays vistos en clase 
CATEGORY
        Analizador de bases de datos 
GITHUB
 https://github.com/Heldrysh/python2_class/blob/master/Tareas/Numpy.py
      
INPUT 
  Los arrays dados en la clase pertenecinetes al ejercicio 1 
OUTPUT 
    3 arrays distintos en uno contendremos los costos, en los que se contendra la produccion,
    los costos y los costos por g/L 
EXAMPLES
  Input:
     produccion = np.array([[5, 3], [11, 7], [4, 9], [2, 6]])
     costos = np.array([3.5, 5, 7, 4.3])
  Output:
    El array ordenado de produccion es: 
     [('gen1',  5, 3) ('gen2', 11, 7) ('gen3',  4, 9) ('gen4',  2, 6)]
    El array ordenado de costos por g/l es: 
     [('gen1', 0.7   , 1.1666) ('gen2', 0.4545, 0.7142)
     ('gen3', 1.75  , 0.777 ) ('gen4', 2.15  , 0.7166)]
     El array ordenado de costos es: 
     [('gen1', 3.5) ('gen 2', 5. ) ('gen3', 7. ) ('gen4', 4.3)]

"""
import numpy as np
#Datos de ingreso (dados en clase)
produccion=np.array([[5,3], [11,7], [4,9], [2,6]])
costos = np.array([3.5, 5, 7, 4.3])
#Para generar los costos pero en g/L usaremos una division entre costo y produccion y su transpuesta
costo_por_gL = (costos / produccion .T)
#Generamos los arrays estructurados 
struc_produccion=  np.array([('gen1', 5, 3), ('gen2', 11,7),('gen3',4,9),('gen4',2,6)],
       dtype=[('gen', (np.str_, 6)), ('Temp1', np.int32), ('temp2', np.int32)])

struc_gL= np.array([('gen1', 0.7, 1.1666), ('gen2', 0.4545,0.7142),('gen3',1.75,0.777),('gen4',2.15,0.7166)],
       dtype=[('gen', (np.str_, 6)), ('temp1', np.float64), ('temp2', np.float64)])

strruc_costos= np.array([('gen1', 3.5), ('gen 2', 5),('gen3',7),('gen4',4.3)],
       dtype=[('gen', (np.str_, 6)), ('costos', np.float64)])

print ("Los arrays estructurados son: \n\n")
print("El array ordenado de produccion es: \n", struc_produccion)
print("El array ordenado de costos por g/l es: \n",struc_gL)
print("El array ordenado de costos es: \n",strruc_costos)


