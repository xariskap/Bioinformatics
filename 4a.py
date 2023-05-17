string = "nanakali"
n = len(string)
c = int((n-1)/2)
for i in range(c):
        #print(string[0],string[c+1],c+1)
        if string[0] == string[c+1] and len(string[0:c+1])==len(string[c+1:c+2+c]):
                print(string[0:c+1],string[c+1:c+2+c])
                if string[:c+1]==string[c+1:c+2+c]:
                        print(string[0:c+1])
                        print("Success")
                        break
        else:
                c -=1
