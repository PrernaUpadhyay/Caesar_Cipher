

---

# Caesar Cipher 🔐

Welcome to the **Caesar Cipher** project! This is a Python program that allows users to encode or decode a message using the famous Caesar Cipher. The cipher shifts each letter in the message by a specified number of positions in the alphabet.

## Features

- **Encode Messages**: Shift letters forward in the alphabet to encrypt the message.
- **Decode Messages**: Shift letters backward to decrypt the message.
- **Preserves Non-Alphabet Characters**: Characters like spaces, numbers, and punctuation are not affected by the shift.
- **User Input for Shift**: Allows flexibility in choosing the shift amount.

## How It Works

1. The user is prompted to choose between encoding or decoding.
2. The program takes the input message and the shift value.
3. It then processes the message based on the Caesar Cipher logic and outputs the result.

### Caesar Cipher Logic:
- Each letter in the message is shifted by the given number of positions.
- If the direction is "encode", the letters are shifted forward.
- If the direction is "decode", the letters are shifted backward.
- The shift is applied modulo 26 (the length of the alphabet) to handle wrap-around.

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/PrernaUpadhyay/Caesar_Cipher.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Caesar_Cipher
   ```
3. Run the Python script:
   ```bash
   python caesar_cipher.py
   ```

## Usage

1. **Type 'encode' to encrypt** or **'decode' to decrypt**.
2. **Enter the message** you want to encode or decode.
3. **Provide a shift number** (an integer value).

### Example:

```bash
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

Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
5
The encoded text is: mjqqt btwqi
```

## Contributing

Feel free to fork the repository and submit pull requests with improvements, features, or bug fixes.

---

