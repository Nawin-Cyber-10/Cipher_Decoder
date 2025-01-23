# algorithms.py

def caesar_encrypt(text, shift):
    """Encrypts text using Caesar Cipher."""
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr((ord(char) + shift_amount - 65) % 26 + 65) if char.isupper() else chr((ord(char) + shift_amount - 97) % 26 + 97)
            result += new_char
        else:
            result += char
    return result

def rail_fence_encrypt(text, key):
    """Encrypts text using Rail Fence Cipher."""
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    direction_down = False
    row, col = 0, 0

    for char in text:
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        rail[row][col] = char
        col += 1

        row += 1 if direction_down else -1

    result = []
    for r in rail:
        result.append(''.join(r).replace('\n', ''))
    return ''.join(result)

def row_matrix_encrypt(text, key):
    """Encrypts text using Row Matrix method."""
    # Fill the matrix
    matrix = [text[i:i + key] for i in range(0, len(text), key)]
    # Transpose the matrix
    encrypted = ''.join([''.join(row[i] for row in matrix if i < len(row)) for i in range(key)])
    return encrypted

def substitution_encrypt(text, mapping):
    """Encrypts text using Substitution Cipher."""
    return ''.join([mapping.get(char, char) for char in text])

def vigenere_encrypt(text, key):
    """Encrypts text using Vigenère Cipher."""
    encrypted = []
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_length].lower()) - ord('a')
            new_char = chr((ord(char.lower()) + shift - 97) % 26 + 97)
            encrypted.append(new_char.upper() if char.isupper() else new_char)
        else:
            encrypted.append(char)
    return ''.join(encrypted)

def caesar_decrypt(text, shift):
    """Decrypts text using Caesar Cipher."""
    return caesar_encrypt(text, -shift)  # Decrypting is just encrypting with a negative shift

def rail_fence_decrypt(ciphertext, key):
    """Decrypts text using Rail Fence Cipher."""
    # To decrypt, we will create the rails first
    rail = [['\n' for _ in range(len(ciphertext))] for _ in range(key)]
    direction_down = None
    row, col = 0, 0

    for char in ciphertext:
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        rail[row][col] = '*'
        col += 1

        row += 1 if direction_down else -1

    index = 0
    for r in range(key):
        for c in range(len(ciphertext)):
            if (rail[r][c] == '*' and index < len(ciphertext)):
                rail[r][c] = ciphertext[index]
                index += 1

    result = []
    row, col = 0, 0
    for char in ciphertext:
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        if rail[row][col] == '*':
            result.append(char)
            col += 1
        row += 1 if direction_down else -1

    return ''.join(result)

def row_matrix_decrypt(ciphertext, key):
    """Decrypts text using Row Matrix method."""
    # Calculate the number of rows
    num_rows = len(ciphertext) // key
    # Fill the matrix
    matrix = ['' for _ in range(num_rows)]
    index = 0
    for r in range(num_rows):
        matrix[r] = ciphertext[index:index + key]
        index += key
    # Read the matrix row-wise
    decrypted = ''.join([''.join(row[i] for row in matrix if i < len(row)) for i in range(key)])
    return decrypted

def substitution_decrypt(text, mapping):
    """Decrypts text using Substitution Cipher."""
    reverse_mapping = {v: k for k, v in mapping.items()}
    return ''.join([reverse_mapping.get(char, char) for char in text])

def vigenere_decrypt(ciphertext, key):
    """Decrypts text using Vigenère Cipher."""
    decrypted = []
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key[i % key_length].lower()) - ord('a')
            new_char = chr((ord(char.lower()) - shift - 97) % 26 + 97)
            decrypted.append(new_char.upper() if char.isupper() else new_char)
        else:
            decrypted.append(char)
    return ''.join(decrypted)
