# Proyecto-Fin-de-Master
*Autor*: Rocío Marugán Pinos, estudiante del Máster en Métodos Computacionales en Ciencias en la Universidad de Navarra (UNAV) durante el curso 2021/2022
Contacto: rmaruganpin@alumni.unav.es

## Objetivo
Combinar los aspectos más útiles de las herramientas de procesado de datos de secuenciación Vicinal (Z Lu, research, & 2014, n.d.) y CirSeq (A Acevedo, Brodsky, Nature, & 2014, n.d.) para desarrollar una nueva que permita (de momento) la detección de circRNAs considerados "pequeños" (< 60 nt) y el mapeo de sus coordenadas genómicas.
Este repositorio contine todos los datos y scripts empleados para ello en orden cronológico, para que sirva de reflejo del trabajo realizado por parte del alumno y para la posible continuación con el proyecto a futuro

*Citaciones*:
Lu, Z, research, A. M.-N. acids, & 2014, undefined. (n.d.). Vicinal: a method for the 
determination of ncRNA ends using chimeric reads from RNA-seq experiments. 
Academic.Oup.Com. Retrieved from https://academic.oup.com/nar/articleabstract/42/9/e79/1257539
Acevedo, A, Brodsky, L., Nature, R. A.-, & 2014, undefined. (n.d.). Mutational and fitness 
landscapes of an RNA virus revealed through population sequencing. Nature.Com. 
Retrieved from https://www.nature.com/articles/nature12861

## Requerimientos
1. Python (posterior a version 2.7.5)    https://www.python.org/ftp/python/2.7.5/Python-2.7.5.tgz
2. Bowtie2 (posterior a version 2.1.0)   http://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.1.0/
* La lista completa de parámetros de Bowtie2 utilizada es: *–sensitive-local –score-min G,2,8 --a
–no-unal -x index_prefix -U filename.fastq -S filename.sam*

## Scripts y Archivos
### intrones_drosophila.txt
Secuencias de 16 intrones circulares de *Drosophila melanogaster* con información sobre su nombre, cromosoma de origen y coordenadas genómicas
### Secuencias de referencia
Carpeta que contiene las secuencias en formato FASTA de todos los cromosomas de *Drosophila melanogaster Release 6 plus 
ISO1 (dm6)* (Release 6 plus ISO1 MT - dm6 - Genome - Assembly - NCBI (nih.gov))
### generacion_reads.py
Script para la simulación de la generación de una librería de secuenciación a partir de una amplificación por rolling circle RT-PCR + fragmentación química aleatoria
### synth_intrones.fastq
Archivo en formato FASTQ resultado de la ejecución del script *generacion_reads.py*
### cirseq_adapt.py
Script adaptado de la herramienta CirSeq para, por un lado, obtener la unidad repetitiva de las lecturas de secuenciación en *synth_intrones.fastq* (*synth_consensus.fastq*) y, por otro, generar un nuevo archivo FASTQ con todas las rotaciones posibles de ese consenso (*synth_rotated.fastq*). Genera también un archivo con la lista de longitudes de cada unidad repetitiva inicial (*repeat_lenght.txt*)
### synth_rotated_local_multi.sam
Archivo en formato SAM resultado del alineamiento con Bowtie2 con los parámetros listados arriba de *synth_rotated.fastq* al índice generado a partir de las secuencias en la carpeta *Secuencias de referencia*
### bowtie2_mapping_results.py
Filtrado de los datos de interés de *synth_rotated_local_multi.sam* a un archivo CSV (*bowtie2_mapping_results.csv*). Genera también una lista de parámetros relacionados con el alineamiento (*bowtie2_mapping_parameters.txt*)
