# COMPLETE EXPLAINATION AT :- https://youtu.be/CuR0DVzToi4
'''
author: cYpHeR
github: cypher-nullbyte
'''
import math
import numpy
import sympy

def modInverse(a, m) :
    a = a % m
    for x in range(1, m) :
        if ((a * x) % m == 1) :
            return x
    return 1
def KeyMatrix(Key,n):
    Matrix=[]
    for i in range(n):
        temp=list()
        for j in range(n):
            temp.append(ord(Key[i*n+j])-97)
        Matrix.append(temp)
    d=math.floor(numpy.linalg.det(Matrix))
    if d==0:
        print("Invalid Key!")
        exit(None)
    A=sympy.Matrix(Matrix)
    A=(A.adjugate()*modInverse(d,26))%26
    for i in range(n):
        for j in range(n):
            Matrix[i][j]=A[i,j]
    return Matrix

def Multiply(X,Y):
    result = numpy.zeros([len(X),1], dtype = int)
    Y=list([ord(x)-97] for x in Y)
    result=numpy.dot(X,Y)
    return result
def Hill_decrypt(Matrix,Cipher,n):
    Plain=""
    for i in range(0,len(Cipher),n):
        temp=Multiply(Matrix,Cipher[i:i+n])
        for x in range(n):
            Plain+=chr(temp[x][0]%26+97)
    return Plain
if __name__=="__main__":
    Key=''.join(input("Enter Key: ").lower().split())
    Cipher=input("Enter CipherText: ")
    n=math.sqrt(len(Key))
    if n!=math.trunc(n) and n!=0:
        print("Invalid key!")
        exit(None)
    n=math.floor(n)
    Matrix=KeyMatrix(Key,n)
    print("PlainText: ",Hill_decrypt(Matrix,Cipher,n))
