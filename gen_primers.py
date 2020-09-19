#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
#import numpy as np


# In[73]:



           
            


# In[48]:


d = {}
with open("codons") as f:
    for line in f:
       (codon, aa, key, w) = line.split()
       d[key] = codon


# In[79]:


def gen_seq(fasta):
    
    n = len(fasta)

    out=""
    #iterate over mutation positions

    for i in range(2,n):
        mod = [1]*n
        # 1: 1st choice; 2: 2nd choice; 0:NNK
        mod[i] = 0

        left = 2
        resi = i
        while left != 0:
            if fasta[resi - 1] != "W" and fasta[resi - 1] != "M":
                mod[resi - 1] = 2
                left -= 1
            resi -= 1

        #mod[i-1] = 2
        #mod[i-2] = 2

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

            


# In[80]:


primers = ""
with open("input.fasta") as f:
    for line in f:
        s = line.split()[0]
        fasta = [i for i in s]
        primers += gen_seq(fasta)


# In[75]:





# In[81]:


f = open("primers.txt","w")
f.write(primers)
f.close


# In[ ]:




