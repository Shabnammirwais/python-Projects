logo = '''
,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88
              88
              88   '''
print(logo)

alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

def ceasar(original_text, shifted_amount, direction):

    if direction == "encode":
        encoded_text = ""
        for char in original_text:
            if char in alphabet:
                shifted_position = alphabet.index(char) + shifted_amount
                shifted_position %= len(alphabet)
                encoded_text += alphabet[shifted_position]
            else:
                encoded_text += char

        print(f"Here is encoded results: {encoded_text}")

    else:
        decoded_text = ""
        for char in original_text:
            if char in alphabet:
                shifted_position = alphabet.index(char) - shifted_amount
                shifted_position %= len(alphabet)
                decoded_text += alphabet[shifted_position]
            else:
                decoded_text += char

        print(f"Here is decoded result: {decoded_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type you message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    ceasar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again otherwise 'no' \n").lower()

    if restart == "no":
        print("Goodbye!")
        should_continue = False
