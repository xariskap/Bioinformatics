import numpy as np
string  = "ababbasdfabbbbb"
n = len(string)
sc_mat = []
j=0
i=1
sc_mat.append(j)
while len(sc_mat)<len(string):
  if string[i] == string[j]:
    
    j+=1
    i+=1
    sc_mat.append(j)
  else:
    if j==0:
      sc_mat.append(0)
      i+=1
    if j!=0:
      j = sc_mat[j-1]
    
i,m =0, getMax(sc_mat)
c = int((m)/2)
if string[:c+1] == string[c+1:m+1]:
  print(string[:c+1], string[c+1:m+1])
