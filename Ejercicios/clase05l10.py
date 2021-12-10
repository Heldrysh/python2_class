"""
clase del 5 de octube
entrez.efetch y taxonomias, fue una clase muy difusa
preguntar despues por dudas
"""
from Bio import Entrez
Entrez.email = "montes355@gmail.com"

termino = "(Aedes[Title] OR Aedes[All Fields])AND((RNA-Seq[Title] OR transcriptomic[Title]) OR (transcriptome[Title] OR sequencing[Title]))"
 handle = Entrez.egquery(term=termino)
 record = Entrez.read(handle)
 handle.close()
 for row in record["eGQueryResult"]:
     print(row["DbName"], row["Count"])
 handle = Entrez.espell(term="biopythooon")
 record = Entrez.read(handle)
 record["Query"]
#Algo de un error
 record["CorrectedQuery"]
#Se corrigio (no se que paso)

#Esummary
 handle = Entrez.esummary(db="taxonomy", id="9913,30521")
 record = Entrez.read(handle)
 handle.close()
 print(record[0].keys())
 print(record[0]["Id"])
 print(len(record))

import pickle
print(len(pickle.dumps(record)))

#efetch
from Bio import Seq.IO
 Entrez.efetch(base de datos, id, tipo, modo)
 handle = Entrez.efetch(db="nucleotide", id="HE805982", rettype="gb", retmode="text")
 record = SeqIO.read(handle, "genbank")
 handle.close()
#


 filename = "HE805982.gb"
#Emulamos handle con el filename
 with Entrez.efetch(db="nucleotide",id="HE805982",rettype="gb", retmode="text") as file:
    with open(filename, "w") as handle:
         handle.write(file.read())
 handle.close()
 record = SeqIO.parse("HE805982.gb", "genbank")
 print(record)

# Debemos usar read.handle en vez de Entrez.read
 out_handle = open("prueba.fasta", "w")
 fetch_handle = Entrez.efetch(db="nucleotide", id="1919569438, 1919569357, 1251949171",
                            rettype="fasta", retmode="text")
 data = fetch_handle.read()  #usar handle.read()
 fetch_handle.close() #cerrar handle
 out_handle.write(data) #escribir archivo
 out_handle.close() #cerrar archivo

#Ejercicio#2
#Buscar linajes, que tan emparentados estan dos organismos siendo "Notoryctes typhlops" y "Chrysochloris asiatica"
handle = Entrez.esearch(db="Taxonomy", term="Notoryctes typhlops")
record = Entrez.read(handle)
print(record["IdList"])
handle.close()
### Con esto, obtenemos el ID del organismo que buscamos en la base de datos de Taxonomy

id_taxo = record["IdList"]
handle = Entrez.efetch(db="Taxonomy", id=id_taxo, retmode="xml")
Notoryctes = Entrez.read(handle)
print(Notoryctes[0].keys())
#Vemos que esta Lineage, que es el que nos interesa, y ponemos
print(Notoryctes[0]["Lineage"])
handle.close()
#Se repite lo mismo con el otro organismo
#Comparamos
handle2 = Entrez.esearch(db="Taxonomy", term="Chrysochloris asiatica")
record2 = Entrez.read(handle2)
id_taxo2 = record2["IdList"]
handle2 = Entrez.efetch(db="Taxonomy", id=id_taxo2, retmode="xml")
Chrysochloris = Entrez.read(handle2)
print(Chrysochloris[0]["Lineage"])
handle2.close()
print(Notoryctes[0]["Lineage"])
Not = (Notoryctes[0]["Lineage"])
Not2 = Not.split(";")
Chrys = (Chrysochloris[0]["Lineage"])
Chrys2 = Chrys.split(";")
def comparar(org1, org2):
    i = 0
    for lin1, lin2 in zip(org1, org2):
        if lin1 == lin2:
            i = i+1
        else:
            break
    return i
print(comparar(Not2, Chrys2))
