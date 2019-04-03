MORSE_CODE = {'.-': 'A',   '-...': 'B',   '-.-.': 'C',
             '-..': 'D',      '.': 'E',   '..-.': 'F',
             '-.': 'G',   '....': 'H',     '..': 'I',
             '.---': 'J',    '-.-': 'K',   '.-..': 'L',
             '--': 'M',     '-.': 'N',    '---': 'O',
             '.--.': 'P',   '--.-': 'Q',    '.-.': 'R',
             '...': 'S',      '-': 'T',    '..-': 'U',
             '...-': 'V',    '.--': 'W',   '-..-': 'X',
             '-.--': 'Y',   '--..': 'Z'}

def decodeMorse(morse_code):
    output = ""
    storage = ""
    blank_count = 0
    for char in morse_code.strip():
        if char != " ":
            storage += char
        else:
            if storage == "":
                blank_count += 1
                if blank_count == 2:
                    output += " "
                    blank_count = 0
            else:
                output += MORSE_CODE[storage]
                storage = ""
    output += MORSE_CODE[storage]
    return output
