def getMax(matrix):
  arr = np.array(matrix)
  return arr.argmax()

def temp(sc_mat):
  zero = []

  for i in range(len(sc_mat)):
    if sc_mat[i] == 0:
      zero.append(i)
    else:
      break
  print(zero)
  result = []
  for i in range(0,len(sc_mat), len(zero)):
    print("String with zero arr:",string[:zero[-1]+1], string[i:i+len(zero)])

    if string[:zero[-1]+1] == string[i:i+len(zero)]:
      result.append( string[i:i+len(zero)])
    else :break
  print(result)

import numpy as np
string  = "aabbcaacbbcaabbabba"
def lps(string):
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
  return sc_mat
sc_mat = lps(string)
i,m =0, getMax(sc_mat)
c = int((m)/2)

if string[:c+1] == string[c+1:m+1]:
  print(string[:c+1], string[c+1:m+1])

else:
  temp(sc_mat[:m+1])
