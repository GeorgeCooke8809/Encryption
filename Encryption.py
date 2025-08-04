def encrypt(plain_text: str, key: str, level: str):
    if key == "":
        key = "L0"
    
    if level == "Lvl. 1":
        encrypted_text = level_one_convert(plain_text, key)
    else:
        encrypted_text = level_two_convert(plain_text, key)

    return encrypted_text

def decrypt(encrypted_text: str, encryption_key: str, level: str):
    if encryption_key == "":
        encryption_key = "L0"

    if encryption_key[0] == "R":
        decryption_key = "L" + encryption_key[1:]
    else:
        decryption_key = "R" + encryption_key[1:]

    if level == "Lvl. 1":
        plain_text = level_one_convert(encrypted_text, decryption_key)
    else:
        plain_text = level_two_convert(encrypted_text, decryption_key)

    return plain_text

def encrypt_alphabet(direction: str, ammount: int):
    plain_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "'", '"', ";", ":", "(", ")", "!", "$", "%", "&", "-", "_", "?", " "]

    ammount = ammount % 78
    new_alphabet = []
    new_alphabet.extend(plain_alphabet)

    if direction == "L":
        new_alphabet.extend(new_alphabet[0:ammount])
        del(new_alphabet[0:ammount])
    else:
        temp = new_alphabet[-ammount:]
        temp.extend(new_alphabet)
        new_alphabet = temp
        del(new_alphabet[-ammount:])

    return new_alphabet

def level_one_convert(text_in: str, key: str):
    plain_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "'", '"', ";", ":", "(", ")", "!", "$", "%", "&", "-", "_", "?", " "]

    try:
        encryption_direction = key[0]
        encryption_ammount = int(key[1:])

        encrypted_alphabet = encrypt_alphabet(encryption_direction, encryption_ammount)

    except: # This will be triggered in the sandbox pages when the key is being typed in so that it does not crash when key is just "L" or "R"
        encrypted_alphabet = plain_alphabet

    encrypted_text = ""

    for i in text_in:
        try:
            position_original_alphabet = plain_alphabet.index(i)
            encrypted_char = encrypted_alphabet[position_original_alphabet]
            encrypted_text += encrypted_char
        except: # This will trigger if a character is not in the alphabet such as "%"
            encrypted_text += i

    return encrypted_text

def level_two_convert(text_in: str, key: str):
    index = 0
    plain_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "'", '"', ";", ":", "(", ")", "!", "$", "%", "&", "-", "_", "?", " "]

    encrypted_text = ""

    if key not in ("L", "R"):
        encryption_direction = key[0]
        key_number = key[1:]
    else:
        encryption_direction = "L"
        key_number = "0"

    key_number_length = len(key_number)


    for i in text_in:
        print(i)

        current_key_index = index % key_number_length
        shift_ammount = int(key_number[current_key_index])

        encrypted_alphabet = encrypt_alphabet(encryption_direction, shift_ammount)

        try:
            position_original_alphabet = plain_alphabet.index(i)
            encrypted_char = encrypted_alphabet[position_original_alphabet]
            encrypted_text += encrypted_char
        except: # This will trigger if a character is not in the alphabet such as "%"
            encrypted_text += i
        
        index += 1

    return encrypted_text