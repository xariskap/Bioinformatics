import numpy as np
s = lambda x, y, i, j: -2 if x[i] != y[j] else 1
g = -2

class globalAlign:
    def __init__(self,str1,str2):
        self.str1,self.str2 =str1, str2
        self.N,self.M = len(str2),len(str1)
        self.Matrix = self.initialize_matrix()
        self.edit_transcript =[]
        self.result = self.traceback(self.M,self.N)

    def initialize_matrix(self):
        m,n = self.M,self.N
        matrix = np.zeros((m+1, n+1))

        for i in range(1, m + 1):
            matrix[i][0] = i * g

        for j in range(1, n + 1):
            matrix[0][j] = j * g

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                align = matrix[i-1][j-1] + s(self.str1, self.str2, i-1, j-1)
                delete = matrix[i-1][j] + g
                insert = matrix[i][j-1] + g

                matrix[i][j] = max(align, delete, insert)

        return matrix
    def traceback(self,n,m):

        matrix = self.Matrix
        
        if m <= 0 or n <=  0:
            return

        matrix = matrix[:n+1,:m+1]
        align = matrix[n-1][m-1] + s(self.str1, self.str2, n-1, m-1)
        delete = matrix[n-1][m] + g
        insert = matrix[n][m-1] + g

        choise = max(align, delete, insert)
        if x[n-1] == y[m-1]:
            self.edit_transcript.insert(0, "M")
            
            return self.traceback(n-1,m-1)
        else:
            if(choise == align):
                self.edit_transcript.insert(0, "R")
                
                return self.traceback(n-1,m-1)
            elif(choise == delete):
                self.edit_transcript.insert(0, "D")
                
                return self.traceback(n-1,m)
            else:
                self.edit_transcript.insert(0, "I")
                
                return self.traceback(n,m-1)

    def stringAlign(self):
        st1 = []
        st2=[]
        for ele in self.edit_transcript[::-1]:
            if len(self.str1)<=0 or len(self.str2)<=0:
                break
            match ele:
                case 'M':
                    st1.append(self.str1[-1])
                    st2.append(self.str2[-1])
                    self.str1 = self.str1[:-1]
                    self.str2= self.str2[:-1]
                case 'I':
                    st1.append('-')
                    st2.append(self.str2[-1])
                    self.str2= self.str2[:-1]
                        
                    
                case 'D':
                    st2.append('-')
                    st1.append(self.str1[-1])
                    self.str1= self.str1[:-1]   
        print(f'\n First string:\t {"".join(st1[::-1])}\
                \nSecond string:\t {"".join(st2[::-1])}')

if __name__ == "__main__":
    
    y='FMDTPLNE'
    x='FKHMEDPLE'
    temp = globalAlign(x,y)
    temp.stringAlign()