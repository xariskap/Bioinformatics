import numpy as np
s = lambda x, y, i, j: -1 if x[i] != y[j] else 1
g = -1

class Aligner:
    def __init__(self, str1, str2):
        self.str1, self.str2 = str1, str2
        self.N, self.M = len(str2), len(str1)
        self.edit_transcript =[]


class GlobalAligner(Aligner):
    def __init__(self, str1, str2):
        super().__init__(str1, str2)

        self.Matrix = self.initialize_matrix()
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
    def traceback(self, n, m):

        matrix = self.Matrix
        
        if m <= 0 or n <=  0:
            return

        matrix = matrix[:n+1, :m+1]
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

class LocalAligner(Aligner):
    def __init__(self,str1, str2):
        super().__init__(str1, str2)

        
        self.Matrix = self.initialize_matrix()
        self.st1, self.st2 = [], []
        m, n = self.get_max(self.Matrix)
        self.result = self.traceback(m, n)

    def initialize_matrix(self):
        m, n = self.M,self.N
        matrix = np.zeros((m+1, n+1))

        for i in range(1, m + 1):
            matrix[i][0] = 0

        for j in range(1, n + 1):
            matrix[0][j] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                align = matrix[i-1][j-1] + s(self.str1, self.str2, i-1, j-1)
                delete = matrix[i-1][j] + g
                insert = matrix[i][j-1] + g

                matrix[i][j] = max(0, align, delete, insert)

        return matrix
    
    def traceback(self, n, m):
        
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
            self.st1.append(self.str1[n-1])
            self.st2.append(self.str2[m-1])
            return self.traceback(n-1, m-1)
        else:
            if(choise == align):
                self.edit_transcript.insert(0, "R")
                
                return self.traceback(n-1, m-1)
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

    def get_max(self, matrix):
        row, column = np.unravel_index(matrix.argmax(), matrix.shape)
        #print(f'The max number is at index {row, column} and it is {matrix[row][column]}')
        return row, column

    def stringAlign(self):
        print(self.edit_transcript)
        print(f'\n First string:\t {"".join(self.st1[::-1])}\
                \nSecond string:\t {"".join(self.st2[::-1])}')
        
    


if __name__ == "__main__":
    
    y = 'FMDTPLNE'
    x = 'FKHMEDPLE'

    z = 'ATATCGACGA'
    w = 'ATCCGAGAATT'

    globalA = GlobalAligner(x, y)
    LocalA = LocalAligner(z, w)
    globalA.stringAlign()
    LocalA.stringAlign()