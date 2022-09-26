# Proyecto-Fin-de-Master
Autor: Rocío Marugán Pinos, estudiante del Máster en Métodos Computacionales en Ciencias en la Universidad de Navarra (UNAV) durante el curso 2021/2022
Contacto: rmaruganpin@alumni.unav.es

------- Objetivo -----------------------------------------------------------------------
Combinar los aspectos más útiles de las herramientas de procesado de datos de secuenciación Vicinal (Z Lu, research, & 2014, n.d.) y CirSeq (A Acevedo, Brodsky, Nature, & 2014, n.d.) para desarrollar una nueva que permita (de momento) la detección de circRNAs considerados "pequeños" (< 60 nt) y el mapeo de sus coordenadas genómicas.
Este repositorio contine todos los datos y scripts empleados para ello en orden cronológico, para que sirva de reflejo del trabajo realizado por parte del alumno y para la posible continuación con el proyecto a futuro

Citaciones:
Lu, Z, research, A. M.-N. acids, & 2014, undefined. (n.d.). Vicinal: a method for the 
determination of ncRNA ends using chimeric reads from RNA-seq experiments. 
Academic.Oup.Com. Retrieved from https://academic.oup.com/nar/articleabstract/42/9/e79/1257539
Acevedo, A, Brodsky, L., Nature, R. A.-, & 2014, undefined. (n.d.). Mutational and fitness 
landscapes of an RNA virus revealed through population sequencing. Nature.Com. 
Retrieved from https://www.nature.com/articles/nature12861

Requerimientos\n
-------- Scripts y Archivos ------------------------------------------------------------------------
intrones_drosophila.txt
>> ConsensusGeneration.py <<
Lo primero es ver si tal cual está va bien:
	$ cd home/manager/Desktop/pruebas_sinteticas/scripts
	$ python ConsensusGeneration.py /home/manager/Desktop/pruebas_sinteticas/files /home/manager/Desktop/pruebas_sinteticas/files/synth_intrones.fastq.gz

>> Bowtie2 <<
	$ cd home/manager/Desktop/Vicinal/trial_runs/pruebas_sinteticas
	$ bowtie2 --sensitive-local --score-min G,2,8 --no-unal -x /home/manager/Desktop/Vicinal/trial_runs/genome/Index/Dmelanogaster -U synth_rotated.fastq -S synth_rotated_local.sam
