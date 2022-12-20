class node:
    def __init__(self,name,left,right):
        self.name=name
        self.left=left
        self.right=right

input=[['x','+',5],['id','add','num']]
i=0
def parseF():
    if input[i][1]=='id':
        return input[i][0]
    elif input[i][1]=='num':
        return input[i][0]

def parseE():
    a=parseF()
    if input[i][1]=='add':
        i+=1
        b=parseF()
        c=node('add',a,b)
        return c
    elif input[i][1]=='sub':
        i+=1
        b=parseF()
        c=node('sub',a,b)
        return c

while i<3:
    parseE()

