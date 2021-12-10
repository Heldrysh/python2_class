"""
Clase biopython del 28/09/2021 
aprendimos el uso de Entrez un modulo en biopython que nos ayuda 
en el acceso a NCBI y posiblemente otras bases de datos 
"""
#Ejercicio#1
from Bio import Entrez
from pprint import pprint # para visualizar más bomnito los diccionarios.

# Ingresamos nuestro correo
Entrez.email = "dmontes@lcg.unam.mx"

handle = Entrez.einfo(db = "genome")
record = Entrez.read(handle)

i = -1
for field in record["DbInfo"]["FieldList"]:
    i += 1
    if field["Name"] == "ORGN":
        print(field["Name"], field["Description"])

print(record["DbInfo"]["FieldList"][9]["Description"])


#esearch

handle = Entrez.esearch(db="pubmed", term="biopython")
record = Entrez.read(handle)
print (record["Count"])
print(handle.url)
handle.close()

#Ejercicio #2
#BUscamos autor
handle = Entrez.esearch(db = "pubmed", term = "Valeria Mateo-Estrada[AUTH]")
record = Entrez.read(handle)
handle.close()