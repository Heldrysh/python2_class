"""
Clase 19/10/2021
Clase preparatoria a una tarea de costos por producto
"""
import numpy as np
ecoli_m_b = np.array([[0.1, 0.15, 0.19, 0.5,  #matraz 250ml
                       0.9, 1.4, 1.8, 2.1, 2.3],
                      [0.1, 0.17, 0.2, 0.53, #biorreactor de 50L
                       0.97, 1.43, 1.8, 2.1,  2.8],
                      [0.1, 0.17, 0.2, 0.52, #otro reactor
                       0.95, 1.41, 1.8, 2.2,  2.8]
                    ])
#para 0.39
ecoli_m_b * 0.39
produccion = np.array([ [5,3], [11, 7], [4, 9], [2, 6]])
costos = np.array([3.5, 5, 7, 4.3])
costos / produccion.T