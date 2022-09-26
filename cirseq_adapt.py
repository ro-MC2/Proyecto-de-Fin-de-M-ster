# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 06:37:07 2022
Adaptación de CirSeq a reads de 100 nt
@author: rochi
"""

#%% Obtención de la unidad repetitiva
from scipy.stats import mode

infile = open("synth_intrones.fastq","r")
outfile1 = open("synth_consensus.fastq","w")
outfile2 = open("repeat_lengths.txt","w")

RepeatLengths = [0]*16
j = 0
while True:
    
    SequenceID = infile.readline().rstrip("\n")

    if SequenceID == "":
        break

    Sequence = infile.readline() 
    Sequence = Sequence.rstrip("\n") 
    EmptyLine = infile.readline() 
    QualityScores = infile.readline() 
    QualityScores = QualityScores.rstrip("\n")
    
    SubstringLengths = []
    
    #Identificación de todos los posibles sets de repeticiones y guardado de su longitud

    i = 1
    while i <= 91:
        Substrings = Sequence.split(Sequence[i:i+8])
        for String in Substrings[1:-1]: #[1:-1] evita los extremos, que probablemente no coincidan con la longitud exacta de repetición
            SubstringLengths.append(len(String))
        i += 1
        
    SubstringLengthsMode = mode(SubstringLengths) 
    RepeatLength = int(SubstringLengthsMode[0][0]) + 8 
    RepeatLengths[j] = RepeatLength
    ConsensusSequence = Sequence[:RepeatLength] 
    
    outfile1.write(SequenceID + ":" + str(RepeatLength) + "\n") 
    outfile1.write(ConsensusSequence + "\n") 
    outfile1.write(EmptyLine) 
    outfile1.write(QualityScores[:len(ConsensusSequence)] + "\n") # recortar los quality scores para que tengan la misma longitud
    
    j = j+1

outfile2.write(str(RepeatLengths))

infile.close()
outfile1.close()
outfile2.close()

#%% Obtención de todas las rotaciones posibles de la unidad repetitiva

def rotate(Sequence):
	i = 0
	while i < len(Sequence):
		outfile3.write("@" + "rotation" + str(i) + SequenceID)
		outfile3.write(Sequence[-i:] + Sequence[:-i] + "\n")
		outfile3.write(EmptyLine)
		outfile3.write(QualityScores)
		i += 1
        
infile = open("synth_consensus.fastq")
outfile3 = open("synth_rotated.fastq","w")

while True:
    
    SequenceID = infile.readline().rstrip("@")    

    if SequenceID == "":
        break
 			
    Sequence = infile.readline() 
    Sequence = Sequence.rstrip("\n") 
    EmptyLine = infile.readline() 
    QualityScores = infile.readline() 
    
    Sequence = rotate(Sequence)
    
infile.close()
outfile3.close()
    

	