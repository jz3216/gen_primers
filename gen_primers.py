#!/usr/bin/env python
# coding: utf-8

d = {}
with open("codons") as f:
    for line in f:
       (codon, aa, key, w) = line.split()
       d[key] = codon
           
def gen_seq(fasta):
    
    n = len(fasta)
    out=""

    #iterate over mutation positions
    for i in range(2,n):
        mod = [1]*n
        # 1: 1st choice; 2: 2nd choice; 0:NNK
        mod[i] = 0

        #mark none MW positions to barcode
        left = 2
        resi = i
        while left != 0:
            if fasta[resi - 1] != "W" and fasta[resi - 1] != "M":
                mod[resi - 1] = 2
                left -= 1
            resi -= 1


        #write each seqs
        seq = ""
        for j in range(n):
            if mod[j] == 1:
                seq += d[fasta[j]]
            if mod[j] == 2:
                seq += d[fasta[j] + "2"]
            if mod[j] == 0:
                seq += "NNK"

        seq += "\n"
        out += seq
           
    return out

#main
primers = ""
with open("input.fasta") as f:
    for line in f:
        s = line.split()[0]
        fasta = [i for i in s]
        primers += gen_seq(fasta)

#write to files
#f = open("primers.txt","w")
#f.write(primers)

with open('primers.txt', 'w') as f:
    f.write(primers)



