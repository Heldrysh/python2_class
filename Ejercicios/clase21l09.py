"""
Clase de 21/09/2021 
En esta clase aprendimos sobre proteinas, plagamiento y analisis a través de radiación
finalmente en la parte de bioinformática entramos a PDB 
"""
# Importar libreria a usar
from Bio import PDB


# Util para parsear
parser = PDB.PDBParser(QUIET=True)

# Metodo para obtener los datos
struc = parser.get_structure('prot_1fat', "./src/1fat.pdb")

# Ver los "hijos"
print(struc.child_dict)
print(struc.child_list)

# Acceder a metadatos
print(struc.header.keys())
print(struc.header['structure_method'])
print(struc.header['resolution'])


## EJERCICIO 1
# Importar a PDB
parser = PDB.PDBParser(QUIET=True)
obj_struc = parser.get_structure('prot_1kcw', "./Downloads//1kcw.pdb")
print(obj_struc.header['structure_method'])
print(obj_struc.header['resolution'])


# Acceder a modelos
for model in struc:
    print(model)

model = struc[0]
print(model)

print(model.child_dict)
print(model.child_list)

# Archivo de resonancia magnética nuclear

struc = parser.get_structure('RMN', "./Downloads/1g03.pdb")

for model in struc:
    print(model)

print(model.child_dict)

# Observar cadenas
for chain in model:
    print(chain)

chain = model['A']
print(chain)
print(chain.child_dict)
print(chain.child.list)

# Residuos
for residue in chain:
    print(residue)

residuo = chain[45]
print(residuo)
print(residuo.get_id()[1])
print(residuo.get_resname())

residuos_int = []
for residue in chain:
    if residuo.get_resname() == 'SER':
        residuos_int.append(residuo)

print(len(residuos_int))

#Ejercicio #2
cys_list = [] #En esta lista vamos a guardar las cys

for modelo in obj_struc:
    for chain in modelo:
        " En cadena A"
        if chain.id == 'A':
            for residuo in chain:
                if residuo.get_resname() == 'CYS':
                    cys_list.append(residuo)


for atom in cys_list[0]:
    print(atom.elemento, atom.identificador)

#Ejercicio #4

for cist_1 in cys_list:
    for cist_2 in cys_list:
        if not (cist_1 == cist_2):
            if (cist_1['SG'] - cist_2['SG']) < 8:
                # Se imprimen las coordenadas de los atomos
                print(cist_1['SG'].coord, cist_2['SG'].coord)
                # pareamos ID's de los residuos 
                print(cist_1.id, cist_2.id)