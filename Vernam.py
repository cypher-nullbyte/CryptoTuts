For Complete Explaination:- https://youtu.be/KEbr0PEXBeU
'''
author: cYpHeR
github: cypher-nullbyte
'''

def Vernam(Plain,Key,Flag):
    result=""
    for i in range(len(Plain)):
        char=Plain[i]
        if(Flag):
            result+=chr((ord(char)-97 +ord(Key[i])-97)%26 +97)
        else:
            result += chr((ord(char) - ord(Key[i])+26) % 26 + 97)
    return result
# assumption:- for simplicity we are only considering lowercase-values and without spaces

if __name__=="__main__":
    Key=''.join(input("Enter Key: ").lower().split())
    Plain=''.join(input("Enter Key: ").lower().split())
    if(len(Key)!=len(Plain)):
        print("Invalid Key!")
        exit(None)
    CipherText=Vernam(Plain,Key,True)
    print("CipherText: ",CipherText)
    print("PlainBack: ",Vernam(CipherText,Key,False))

