# ASCII Art Logo
logo = r"""
  ___ __ _  ___  ___  __ _ _ __ 
 / __/ _` |/ _ \/ __|/ _` | '__|
| (_| (_| |  __/\__ \ (_| | |   
 \___\__,_|\___||___/\__,_|_|   

      _       _               
     (_)     | |              
  ___ _ _ __ | |__   ___ _ __ 
 / __| | '_ \| '_ \ / _ \ '__|
| (__| | |_) | | | |  __/ |   
 \___|_| .__/|_| |_|\___|_|   
       | |                    
       |_|                    
"""

# List of lowercase alphabet letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']

def caesar_cipher(text, shift, direction):
    result = ""  # Initialize the result string

    # Adjust shift for decoding
    if direction == "decode":
        shift = -shift

    # Process each character in the input text
    for char in text:
        if char in alphabet:  # If the character is in the alphabet
            index = alphabet.index(char)  # Find the character's index
            new_index = (index + shift) % 26  # Calculate the new index
            result += alphabet[new_index]  # Add the shifted character to result
        else:
            result += char  # If character is not in alphabet, leave it unchanged

    return result  # Return the final encoded/decoded message

# Display ASCII art logo
print(logo)

# Get user input
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Call the function and print the result
output = caesar_cipher(text, shift, direction)
print(f"The {direction}d text is: {output}")
