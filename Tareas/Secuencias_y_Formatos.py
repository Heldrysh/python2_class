"""
NAME
       Secuencias_y_Formatos.py
VERSION
        0.1
AUTHOR
        Diego Montes Gabriel <<dmontes@lcg.unam.mx>>
DESCRIPTION 
        El programa recibe datos de GenkBank, dentro de ella una lista de genes y regresa como output
        el nombre de cada gen, los 15 nucleotidos al inicio de cada secuencia, y la transcripcion y 
        traduccion de esas 15 bases 
CATEGORY
        Analyzer
FUNCTIONS
      resumen(path,genes): 
     [Imprime Organismo Versión de la secuencia
     Fuente del aislado
     País
      Para cada gen en la lista:
      Nombre del gen
     Los primeros 15 nucleótidos de ADN
     Los primeros 15 nucleótidos de ARN
     Los primeros 15 aminoácidos de proteína]
GITHUB
  https://github.com/Heldrysh/python2_class/edit/master/Tareas/Secuencias_y_Formatos.py
INPUT 
  Recibimos un archivo de GeenBank con una lista de genes 
OUTPUT 
    El programa da como output el organismo analizado, la version de la secuencia, fuente del aisalado, traduccion
    y transcripcion de las 15 bases iniciales de cada gen dentro de la lista.
EXAMPLES
    Input:
      path = "../files/ambystoma.gb"
      Gen = ["D","H","M","G"]
"""
from Bio.Seq import Seq
from Bio import SeqIO

# Definimos la función La funcion es definida con los parametros de path y genes 
def resumen(path, genes):

    #Toda la informacion a mostrar sera obetenida de los metadatos de GenBank
    for metadato in SeqIO.parse(path, "GenBank"):
        especimen = metadato.annotations['organismo']
        print('Organismo que se obtiene de metadatos: ' + especimen)
        data = metadato.annotations['data']
        print('Fecha de obtencion de la muestra: ' + data)
      # Imprimimos el pais de la obtencion de la muestra
        country = metadato.features[0].qualifiers['country']
        print('Pais donde se obtuo la muestra muestra: ' + str(country))

        # Obtiene e imprime el orden de los aisalados
        Numero_del_aislado = metadato.features[0].qualifiers['Numero_del_aislado']
        print('El numero del aislado ' + str(Numero_del_aislado) + '\n')

        # Comenzamos el parseo tomando en cuenta que los genes van de 2 en 2
        for num in range(1, len(metadato.features), 2):

            # Recorremos los genes en busqueda de su identificacion 
            for gene in genes:

                # Encontramos el gen buscado e imprimimos su traduccion y transcipcion 
                if metadato.features[num].qualifiers['gene'][0] == gene:

                    # Nombre de los genes
                    nombre_del_gen = metadato.features[num].qualifiers['gene']
                    print('Nombre del gen: ' + str(nombre_del_gen))

                    # Obtenemos la transcripcion y traduccion de los primero 15 nutleotidos de cada gen 
                    inicio = metadato.features[num].location.nofuzzy_start
                    final = inicio + 15
                    DNA = metadato.seq[inicio:final]
                    print(DNA)
                    RNA = DNA.transcribe()
                    print(RNA)
                    PROT = RNA.translate()
                    print(PROT, '\n')


# Codigo principal en el que llamamos a la funcion y especificamos el path, para la busqueda de genes 
path = "../data/virus.gb"
genes = ['L', 'N']
resumen(path, genes)
