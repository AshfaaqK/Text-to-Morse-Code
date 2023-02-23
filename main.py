# Dictionary of alhpabet with values of morse
morse_dict = {'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.', 'F': '.._.', 'G': '__.', 'H': '....',
              'I': '..', 'J': '.___', 'K': '_._', 'L': '._..', 'M': '__', 'N': '_.', 'O': '___', 'P': '.__.',
              'Q': '__._', 'R': '._.', 'S': '...', 'T': '_', 'U': '.._', 'V': '..._', 'W': '.__', 'X': '_.._',
              'Y': '_.__', 'Z': '__..', '1': '.____', '2': '..___', '3': '...__', '4': '...._', '5': '.....',
              '6': '_....', '7': '__...', '8': '___..', '9': '____.', '0': '_____'}

# Input for what will be translated into morse
sentence = input('Enter what you want to be translated:\n').upper()

# Scrubs string of any characters not in the morse alphabet
for letter in sentence:
    if letter not in morse_dict:
        sentence = sentence.replace(letter, '')


def translate_to_morse(string):
    """Takes input 'string' and converts every character to morse and returns one value which is the encoded string"""
    translated = ''

    # Fetches the value for every character key in the string and concatenates it at the end of the variable translated
    for char in string:
        translated = translated + morse_dict[char] + '  '

    return translated


# Output morse code
print(translate_to_morse(sentence))
