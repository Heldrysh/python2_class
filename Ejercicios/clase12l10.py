"""
Clase del 12/10/21 
Fue una clase sobre Expasy 
get_prodoc_entry Interface to the get-prodoc-entry CGI script.
get_prosite_entry Interface to the get-prosite-entry CGI script.
get_prosite_raw Interface to the get-prosite-raw CGI script.
get_sprot_raw Interface to the get-sprot-raw CGI script.
"""
from Bio import Entrez, SeqIO
Entrez.email = "montes355@gmail.com"
handle = Entrez.esearch(db="protein", term="Aedes aegypti[Orgn] AND APY[Gene]")
record = Entrez.read(handle)
print(record["Count"])
print(record['IdList'])
handle2 = Entrez.efetch(db="protein", id="193806340", rettype="gb", retmode="text")
record2 = SeqIO.read(handle2, "genbank")
handle2.close()
print(record2.id)
print(record2.annotations['db_source'])
db_source = record2.annotations['db_source']
print(db_source)
apy_prot = record2.annotations['accessions']
print(apy_prot)

handle3 = Entrez.esearch(db="gene", term="Aedes aegypti[Orgn] AND apy[Gene]")
record3 = Entrez.read(handle3)
handle3 = Entrez.efetch(db="gene", id=record3['IdList'][0], retmode="xml")
record3 = Entrez.read(handle3, "genbank")
print(record3[0]['Entrezgene_gene']['Gene-ref']['Gene-ref_syn'])
sinonimos = record3[0]['Entrezgene_gene']['Gene-ref']['Gene-ref_syn']
print([uniprot for uniprot in sinonimos if '_' in uniprot])

#Ejercicio#1
handle4=Entrez.esearch(db = "protein", term = "Aedes aegypti[Orgn] AND apy[Gene]")
record4 = Entrez.read(handle4)
print(record4["Count"])
print(record4["IdList"])

handle4 = Entrez.efetch(db="protein", id=record4['IdList'][0], rettype="gb", retmode="text")
record4 = SeqIO.read(handle4, "genbank")
print(record4.annotations["db_source"])# se arreglo algo

from Bio import ExPASy
from Bio import SwissProt

apy_prot = ['P50635']
handle = ExPASy.get_sprot_raw(apy_prot)
print(handle.url)
record = SwissProt.read(handle)
print(record.__dict__.keys())

db_source.split(';')[0]
handle = ExPASy.get_sprot_raw('APY_AEDAE')
record = SwissProt.read(handle)
print (record.entry_name)
print(record.sequence_length)

#Ejercicio#2
handle = ExPASy.get_sprot_raw('P91793')
record = SwissProt.read(handle)
print(record.created)
print(record.annotation_update)
print(record.taxonomy_id)

#Objeto con SeqRoecord
import Bio.SeqRecord, Bio.Seq
seqRec = Bio.SeqRecord.SeqRecord(seq=Bio.Seq.Seq(record.sequence),
                                 id=record.entry_name,
                                 name=record.organism,
                                 description=record.description)
print(seqRec.format('fasta'))

#Bio.Sequtils Calculate the molecular mass of DNA, RNA or protein sequences as float.
#Only unambiguous letters are allowed. Nucleotide sequences are assumed to have a 5' phosphate.
from Bio.SeqUtils import seq3, seq1, molecular_weight
prot = seqRec.seq
print(seq3(prot)[0:12])
print(seq1(prot)[0:12])
print(molecular_weight(prot, seq_type='protein'))

#Ejercicio#3
objeto_SeqRecord = Bio.SeqRecord.SeqRecord( seq=Bio.Seq.Seq(record.sequence),
                                 id=record.entry_name,
                                 name=record.organism,
                                 description=record.description)
for key, item in objeto_SeqRecord.__dict__.items():
    print(key, item)
print(objeto_SeqRecord.format('fasta'))
#Evitamos la perdida de informacion que si nos daria swissprot
handle = ExPASy.get_sprot_raw('P91793')
record = SeqIO.read(handle, 'swiss')
print(record.__dict__.keys())

#ME perdi
import Bio.SeqRecord, Bio.Seq
 help(Bio.SeqRecord.SeqRecord)
import Bio.SwissProt
help(Bio.SwissProt.Record)
#Entrar a prosite PROSITE consists of documentation entries describing protein domains, families and functional sites as well as associated patterns and profiles to identify them 
for reference in record.cross_references:
    if 'PROSITE' in reference:
        print(reference)
######DIVISIONXDXDXD
from Bio import ExPASy
from Bio.ExPASy import Prosite
handle = ExPASy.get_prosite_raw("PS00785")
record = Prosite.read(handle)
print (record.name)
print (record.type)
print (record.pattern)
print (record.rules)

from Bio.ExPASy import Prodoc
handle = ExPASy.get_prosite_raw(record.pdoc)
record = Prodoc.read(handle)
print(record.text.replace('\\n','\n'))

#Scan prosite
sequence = "MEHKEVVLLLLLFLKSGQGEPLDDYVNTQGASLFSVTKKQLGAGSIEECAAKCEEDEEFTCRAFQYHSKEQQCVIMAENRKSSIIIRMRDVVLFEKKVYLSECKTGNGKNYRGTMSKTKN"
from Bio.ExPASy import ScanProsite
handle = ScanProsite.scan(seq=sequence)
result = ScanProsite.read(handle)
type(result)
print(result[0])

### Extraer la informacion
handle = ExPASy.get_prosite_raw("PS50948")
record = Prosite.read(handle)
print(record.name)
###Sintaxis
#handle = ExPASy.get_prosite_raw(record.pdoc)
#record = Prodoc.read(handle)