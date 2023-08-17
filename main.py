letter_morse_dict = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    "'": '.----.',
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    ':': '---...',
    '-': '-....-',
    ' ': '   '
}


user_input = input('What would you like to translate ? ')

if user_input[0] == '.' or user_input[0] == '-':
    # Convert from morse to text
    message = []
    morse_letter_dict = {morse: letter for letter, morse in letter_morse_dict.items()}
    words = user_input.split('   ')

    for word in words:
        letters = word.split(' ')

        for letter in letters:
            text = morse_letter_dict[letter]
            message.append(text)
        # Add spacing between each word detected
        message.append(' ')
    print(''.join(message))


else:
    # Convert from text to morse
    morse_code = []
    for letter in user_input:
        morse = letter_morse_dict[letter.upper()]
        if letter != ' ':
            morse_code.append(morse)
            morse_code.append(' ')
        else:
            morse_code.append('  ')

    # Remove the space created after the last morse letter
    if morse_code[-1] == ' ':
        morse_code.pop(-1)
    print("".join(morse_code))
