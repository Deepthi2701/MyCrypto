def cryptoMachine():
    
    alphaNum = 'abcdefghijklmnopqrstuvwxyz0123456789 *'
    key = alphaNum[-1] + alphaNum[0:-1]

    inputText = input("Enter the message you want to encrypt or decrpyt : ")
        
    Dict_E = dict(zip(alphaNum,key))
    Dict_D = dict(zip(key,alphaNum))

    inputMode = input("Enter what you want to do with the input text : 1. Encode (E)   2. Decode (D) ")
 
    if inputMode.upper() == 'E' : 
        ans = ''.join([Dict_E[letter] for letter in inputText.lower()])

    elif inputMode.upper() == 'D' :    
        ans = ''.join([Dict_D[letter] for letter in inputText.lower()])

    else : 
        print("Invalid input - Enter either E (Encryption) or D (Decryption)")

    return ans       

print(cryptoMachine())     