# Ejercicio 3

from Bio.Seq import Seq
from Bio import SeqIO

path = "files/sample.fastq"
# lista para guardar ids de los record que no cumplen con el umbral.
mala_calidad = []
umbral = 40


for record in SeqIO.parse(path, "fastq"):
    promedio = sum(record.letter_annotations["phred_quality"])/len(record.letter_annotations["phred_quality"])
    if (promedio < umbral):
        mala_calidad.append(((promedio, record.id)))


# Genbank?

from Bio import SeqIO

for i in SeqIO.parse("files/aichi.gb", "genbank"):
    print("ID", i.id)
    print ("Secuencia", str(i.seq)[0:30], "...")
    print ("Longitud", len(i))


for j, k in i.annotations.items():
    print(j, k)

#El ejercicio de GenBank

from Bio import SeqIO

path = "files/virus.gb"

for record in SeqIO.parse(path, "genbank"):
    print("ID", record.id)

print(record.annotations)

'''
for key, value in record.annotations:
    print (key, value)
'''
version = record.annotations["sequence_version"]
organismo = record.annotations["organism"]


f_source = record.features[0].qualifiers
f_cds = record.features[1]

print (f_source.location)
print(f_source.type)
print(f_source.qualifiers)

# Ejercicio 4

for virus in SeqIO.parse("../data/virus.gb", "genbank"):
    print(virus.annotations['sequence_version'])
    print(virus.annotations['organism'])
# Ejercicio 5

fuente_aislado = virus.features[0].qualifiers['isolation_source']
pais = virus.features[0].qualifiers['country']