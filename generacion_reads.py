# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 17:47:32 2022
Title: resultados de secuenciación sintéticos a partir de intrones de Drosophila 
circularizados y amplificados para generar tandem repeats unidos en un único 
fragmento simulando el resultado de una "rolling circle" RT-PCR 
@author: rochi
"""

# Importación de módulos
import random
from random import randint
random.seed(123)

# Asignación de parámetros
read_len = 100
tand_cycles = 20
reads_per_intron = 100

# Definición de funciones

def rt_pcr(intron):
    # Posición inicial del sitio de unión aleatorio del primer
    r_primer_strt = randint(1,len(intron)) # se va a utilizar de índice negativo, 
    # por lo que puede ir de 1 a la longitud del read (van incluidos ambos)
    # Resultado de RT-PCR (1 vuelta)
    intron_swap = intron[-r_primer_strt:] + intron[:-r_primer_strt]
    # Generación de los tandem repeats cortando al alcanzar el tamaño de read
    intron_tand = intron_swap * tand_cycles
    return intron_tand

# Fragmentación química

def frag_quimica(intron,intron_tand):
    r_frag_strt = randint(1,len(intron))
    intron_read = intron_tand[r_frag_strt:r_frag_strt+read_len]
    return intron_read

infile = open("intrones_drosophila.txt","r")
outfile = open("synth_intrones.fastq","w")

for line in infile:
    # Guardar por separado el encabezado y la secuencia
    if line[0] == ">":
        header = line
    
    else:
        intron = line.strip("\n") 
        
        # Obtener el tandem repeat
        intron_tand = rt_pcr(intron) 
        
        # Generar 100 resultados diferentes de fragmentación química por intron
        intron_read = frag_quimica(intron, intron_tand)
    
        outfile.write("@" + header)
        outfile.write(intron_read + "\n")
        outfile.write("+" + "\n") 
        outfile.write("H"*read_len + "\n")

infile.close()
outfile.close()


