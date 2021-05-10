def caesar_enc(text,s): 
    result = ""
    for i in range(len(text)): 
        char = text[i] 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
        elif (char.islower()):
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result+=chr((ord(char)))
    return result

def caesar_dec(text,s):
    s=26-s 
    result = ""
    for i in range(len(text)): 
        char = text[i] 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
        elif(char.islower()): 
            result += chr((ord(char) + s - 97) % 26 + 97) 
        else:
            result+=chr((ord(char)))
    return result
