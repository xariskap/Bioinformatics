string  = "abacabacskla"
n = len(string)
sc_mat = []
j=0
sc_mat.append(j)
for i in range(1,n):
  if string[i] == string[j]:
    
    j+=1
    sc_mat.append(j)
  else:
    j=0
    sc_mat.append(j)
    
print(sc_mat)