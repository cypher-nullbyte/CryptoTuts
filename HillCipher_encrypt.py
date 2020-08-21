#    SEE COMPLETE EXPLAINATION :- https://youtu.be/Y_UFbwClcEc
'''
author: cYpHeR
github: cypher-nullbyte
'''
#---------------
# TO KEEP VIDEO SHORT AND SIMPLE, I'LL ELABORATE MAIN POINTS(ON WHITEBOARD) TOWARDS THE END
# I'D SUGGEST U WRITING CODE ALONG WITH ME, AND THEREAFTER REVISIT YOUR CODE WHEN I EXPLAIN @END
#--------------

# pip3 install numpy (TO GET NUMPY)
import math
import numpy
def KeyMatrix(Key,n):
    Matrix=[]
    for i in range(n):
        temp=list()
        for j in range(n):
            temp.append(ord(Key[i*n+j])-97)
        Matrix.append(temp)
    if numpy.linalg.det(Matrix)==0:
        print("Invalid Key!")
        exit(None)
    return Matrix
def Multiply(X,Y):
    Y=list([ord(x)-97] for x in Y)
    result=numpy.zeros([len(Y),1],dtype=int)
    result=numpy.dot(X,Y)
    return result



def Hill_encrypt(Plain,Matrix,n):
    cipher=""
    for i in range(0,len(Plain),n):
        temp=Multiply(Matrix,Plain[i:i+n]) #desp 2
        for x in range(n):
            cipher+=chr(temp[x][0]%26 +97)
    return cipher


# lowercase no-space
if __name__=="__main__":
    Key=''.join(input("Key: ").lower().split())
    Plain=''.join(input("PlainText: ").lower().split())
    n=math.sqrt(len(Key))
    if n!=math.trunc(n) or n==0:
        print("Invalid Key!")
        exit(None)
    n=math.floor(n)
    for i in range(n-len(Plain)%n): # expln1
        Plain+='x'
    Matrix=KeyMatrix(Key,n)
    # print(Matrix)
    print("CipherText: ",Hill_encrypt(Plain,Matrix,n))
