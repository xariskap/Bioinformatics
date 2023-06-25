import numpy as np

def getMax(matrix):
  arr = np.array(matrix)
  return arr.argmax()


string  = "banabanabna"
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
c = int((m-1)/2)
print(sc_mat)
if string[:c+1] == string[c+1:c+len(string[:c+1])+1]:
  print("The longest tandem repeat is: ",end="")
  print( string[c+1:c+len(string[:c+1])+1])
else:
  print("There is no tandem repeat")

