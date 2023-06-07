import numpy as np
s = lambda x, y, i, j: -1 if x[i] != y[j] else 1
g = -1


class LocalAlign:
    def __init__(self,str1,str2):
        self.str1,self.str2 =str1, str2
        self.N,self.M = len(str2),len(str1)
        self.Matrix = self.initialize_matrix()
        self.edit_transcript =[]
        self.st1,self.st2 = [],[]
        self.score = 0
        m, n = self.getMax(self.Matrix)
        self.result = self.traceback(m, n)
        

    def initialize_matrix(self):
        m,n = self.M,self.N
        matrix = np.zeros((m+1, n+1))

        for i in range(1, m + 1):
            matrix[i][0] =0

        for j in range(1, n + 1):
            matrix[0][j] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                align = matrix[i-1][j-1] + s(self.str1, self.str2, i-1, j-1)
                delete = matrix[i-1][j] + g
                insert = matrix[i][j-1] + g

                matrix[i][j] = max(0,align, delete, insert)

        print(matrix)
        return matrix
    def traceback(self,n,m):
        
        matrix = self.Matrix
        if m <= 0 or n <=  0:
            return
        if matrix[n][m] == 0:
            return

        matrix = matrix[:n+1,:m+1]
        align = matrix[n-1][m-1] + s(self.str1, self.str2, n-1, m-1)
        delete = matrix[n-1][m] + g
        insert = matrix[n][m-1] + g

        choise = max(align, delete, insert)
        if x[n-1] == y[m-1]:
            self.edit_transcript.insert(0, "M")
            self.score += 1
            self.st1.append(self.str1[n-1])
            self.st2.append(self.str2[m-1])
            return self.traceback(n-1,m-1)
            
        else:
            if(choise == align):
                self.edit_transcript.insert(0, "R")
                
                return self.traceback(n-1,m-1)
            elif(choise == delete):
                self.edit_transcript.insert(0, "D")
                self.st2.append('-')
                self.st1.append(self.str1[n-1])
                return self.traceback(n-1,m)
            else:
                self.edit_transcript.insert(0, "I")
                self.st1.append('-')
                
                self.st2.append(self.str2[m-1])
                return self.traceback(n,m-1)
    
    def getMax(self, matrix):

        row, column = np.unravel_index(matrix.argmax(), matrix.shape)
        return row, column
    
    
    def stringAlign(self):
        symbols = []
        for i in range(len(self.st1)):
            if self.st1[i] == self.st2[i]:
                symbols.insert(0,"|")
            else:
                symbols.insert(0," ")
        print(f'\n{" ".join(self.st1[::-1])}\n{" ".join(symbols)}\n{" ".join(self.st2[::-1])}')
        print(f"\nThe matching score is {self.score}\n")


if __name__ == "__main__":
    
    y='ATATCGACGA'
    x='ATCCGAGAATT'
    temp = LocalAlign(x,y)
    temp.stringAlign()

    