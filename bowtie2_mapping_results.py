# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 21:10:43 2022
Simplificación para su análisis más sencillo de los mapeos con Bowtie2 a la
secuencia de referencia
@author: rochi
"""
#%% Formatear archivo SAM procedente de reads tras obtener secuencia consenso

infile = open("synth_consensus_local_multi.sam","r")
outfile = open("bowtie2_mapping_results.csv","w")

outfile.write("Intron;" + "Ref_mapeo;" + "Ref_anotacion;" + "Pos_mapeo;" + "Pos_anotacion;" + "CIGAR\n")

for line in infile:
    line = line.split()
    
    if line[0][0] != "@":
        read_name = line[0].split(";")
        real_position = read_name[2].split(":")
        real_position_1 = real_position[0]
        new_line = line[0][1:8] + ";" + line[2] + ";" + real_position[1] + ";" + line[3] + ";" + real_position_1 + ";" + line[5] + "\n"
        outfile.write(new_line)

infile.close()
outfile.close()

#%% Formatear archivo SAM procedente de reads tras obtener secuencia consenso y rotaciones

# Parámetros
n_introns = 16

infile = open("synth_rotated_local_multi.sam","r")
outfile = open("bowtie2_mapping_results.csv","w")
outfile2 = open("bowtie2_mapping_parameters.txt","w")

outfile.write("Rotacion;" + "Intron;" + "Ref_mapeo;" + "Ref_anotacion;" + "Pos_mapeo;" + "Pos_anotacion;" + "CIGAR;" + "Hit\n")

intron_name = ">CR31987"
n_rotations_mapped = 0 # contabilizar las rotaciones de un mismo consenso que mapean
n_rotations_per_intron = []
intron_names = []

for line in infile:
    line = line.split()
    
    if line[0][0] != "@":
        read_name = line[0].split(";")
        rotation = read_name[0].split("@")[0]
        
        if intron_name != read_name[0].split("@")[1]:
            n_rotations_per_intron.append(n_rotations_mapped)
            n_rotations_mapped = 0
            intron_names.append(intron_name)
            
        else:
            n_rotations_mapped += 1
            
        intron_name = read_name[0].split("@")[1]
        real_position = read_name[2].split(":")
        real_position_1 = real_position[0]
        
        if line[3][:2] == real_position_1.replace(",","")[:2]:
            hit = "yes"
        else:
            hit = "no"
        new_line = rotation + ";" + read_name[0].split("@")[1] + ";" + line[2] + ";" + read_name[1] + ";" + line[3] + ";" + real_position_1.replace(",","") + ";" + line[5] + ";" + hit + "\n"
        outfile.write(new_line)

n_rotations_per_intron.append(n_rotations_mapped)
intron_names.append(intron_name)

# Contabilizar los intrones con al menos 1 rotación mapeada
n_introns_mapped = len([elem for elem in n_rotations_per_intron if elem > 0])
prcntg_introns_mapped = (n_introns_mapped/n_introns)*100
outfile2.write("% de intrones mapeados " + str(prcntg_introns_mapped) + "\n")
outfile2.write("Nombre del intron\n")
outfile2.write(str(intron_names) + "\n")
outfile2.write("Nº rotaciones mapeadas\n")
outfile2.write(str(n_rotations_per_intron))

infile.close()
outfile.close()
outfile2.close()
