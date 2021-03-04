#This assignment is a project that would simply convert text into morse code.
#At the start of the project you will see a dictionary of morse code to be accessed
#Then, the text will be encrypted in morse assigning each value
#It then proceedes to decrpyt the code and print it out


MORSEDICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-', ' ': '- '} 
def encrypt(text): 
    cipher = '' 
    for letter in text: 
        if letter != ' ': 
            cipher += MORSEDICT[letter] + ' '
        else: 
            cipher += ' '
  
    return cipher 
  

def decrypt(text): 

    text += ' '
  
    decipher = '' 
    citext = '' 
    global i
    for letter in text: 
  
        i = 0
        if (letter != ' '): 
  

           
            i = 0
  
            citext += letter 
  
        else: 
            
            i += 1
  
            if i == 2 : 
  
                decipher += ' '
            else: 
  
                decipher += list(MORSEDICT.keys())[list(MORSEDICT 
                .values()).index('- ')] 
                citext = '' 
  
    return decipher 
  
def main(): 
    text = input("Enter text here: ")
    result = encrypt(text.upper()) 
    print ("your text in morse code: "+result) 
  
    text = "  "
    result = decrypt(text) 
    print (result) 
  
if __name__ == '__main__': 
    main() 