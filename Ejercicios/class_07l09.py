"""
Clase 07/09/2021
"""
from Bio.Seq import Seq, MutableSeq

seqobj = Seq("ATCGATTGACCC")
mutable = MutableSeq(str(seqobj))
mutable[0] = 'n'

seqobj.complement()
seqobj.reverse_complement()
seqobj.translate(to_stop=True)
seqobj.translate()

seqobj.transcribe()

import re #This module provides regular expression matching operations similar to those found in Perl. 
#It supports both 8-bit and Unicode strings; both the pattern and the strings being processed can 
# contain null bytes and characters outside the US ASCII range.


for codon in re.findall(r"(.{3})", str(seqobj)):
    print(codon)

from Bio.SeqUtils import nt_search

patron = Seq("ACG")
sequence = Seq("ATGATGACGAAACGT")
nt_search(str(sequence), patron)

###############################

# Ejercicio 1

seq = Seq("AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG")
patron = Seq("ATG")
resultados = nt_search(str(seq), patron)

# Posibles ORFs empiezan en esas posiciones
for i in resultados[1:]:
    print(seq[i:].translate(to_stop=True))

## Ejercicio1 

# Se guardan las cadenas y checamos la mas grnade
proteinas = []
for i in resultados[1:]:
    proteinas.append(seq[i:].translate(to_stop=True))

len_proteinas = [len(prot) for prot in proteinas]
len_proteinas = dict(zip(len_proteinas, proteinas))
#ENcontramos la mas grnade 
n = max(len_proteinas.keys())  
len_proteinas[n]

"""
Importación de biopython y seqi0: The main function is Bio.SeqIO.parse(...)
which takes an input file handle (or in recent versions of Biopython alternatively a filename as a string),
 and format string. This returns an iterator giving SeqRecord objects
"""

from Bio import SeqIO

filename = "../data/seq.nt.fa"

for seq_record in SeqIO.parse(filename, "fasta"):
    print(f"ID {seq_record.id}")
    print(f"len {len(seq_record)}")
    print(f"Traduccion {seq_record.seq.translate()}")

#-------------

#Ejercicio #2

id_dict = SeqIO.to_dict(SeqIO.parse(filename, "fasta"))
for i in id_dict:
    print(f">{i}")
    sec = id_dict[i].seq
    for codon in re.findall(r".{3}", str(sec)):
        print(codon, end = "\t")
    print("\n")

#-------------

id_list = list(SeqIO.parse(filename, "fasta"))

record_dict = SeqIO.index(filename, "fasta")
record_dict['seq1']


n = 0
for record in SeqIO.parse("../data/sample.fastq", "fastq"):
    if n < 2:
        print(f"{record.id}, {record.seq}")
        n += 1
    else:
        break
print(record.letter_annotations["phred_quality"])

# Ejercicio#3
import numpy as np #An array object of arbitrary homogeneous items
#Fast mathematical operations over arrays
#Linear Algebra, Fourier Transforms, Random Number Generation

low_qual, total = 0, 0
phred_cutoff = 33

for record in SeqIO.parse("../data/sample.fastq", "fastq"):
    mean_val = np.mean(record.letter_annotations["phred_quality"])
    if mean_val < phred_cutoff:
        low_qual += 1
    total += 1

print(f"La cantidad de lecturas con calidad promedio menor a {phred_cutoff} es {low_qual}, "
      f"de un total de {total} lecturas. ")