alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
    'v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
    'q','r','s','t','u','v','w','x','y','z'
    ]

def caeser(text, shift, direction):
    cipher_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == "encode":
                new_position = position + shift
            else:
                new_position = position - shift
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Here's the {direction}d result: {cipher_text}")

choice = "yes"
while choice.lower() == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number\n"))
    shift = shift % 26

    if direction.lower() == "encode" or direction.lower() == "decode":
        caeser(text,shift,direction)
    else:
        print("Invalid direction, try again")
    
    choice = input("Do you want to encode / decode more? Type 'yes' or 'no'\n")
    if choice != "yes":
        print("Goodbye!")
        break
