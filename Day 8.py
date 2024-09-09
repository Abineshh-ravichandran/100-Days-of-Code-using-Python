logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo)
def encrypt(text, shift):
    shift %= 26
    key_text = alphabet[shift:]+alphabet[:shift]
    encrypted = ""
    for letters in text:
        encrypted += key_text[alphabet.index(letters)]
    return encrypted

def decode(text,shift):
    shift %= 26
    key_text = alphabet[shift:] + alphabet[:shift]
    decoded = ""
    for letters in text:
        letters += alphabet[key_text.index(letters)]
    return decoded

choice = "yes"

while choice == "yes":

    direction = input("Type 'encode' to encrypt and 'decode' to decrypt ")
    text = input("Type your message: ")
    shift = int(input("Type your shift number: "))

    if direction.lower() == 'encode':
        solution = encrypt(text, shift)
        print(f"Here's is the {direction}d result: ",solution)

    elif direction.lower() == 'decode':
        solution = decode(text,shift)
        print(f"Here's is the {direction}d result: ",solution)

    else:
        print("Enter a valid choice")
    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()
print("Good bye ")