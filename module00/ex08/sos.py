import sys

class morse_traductor:
    def __init__(self):
        self.morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
            '8': '---..', '9': '----.', ' ': '/'
        }

    def translate_to_morse(self, text):
        morse_code = []
        for char in text:
            if char.upper() in self.morse_dict:
                morse_code.append(self.morse_dict[char.upper()])
                print(morse_code)
        return ' '.join(morse_code)


def main():
    s = " "
    mt = morse_traductor()
    if len(sys.argv) == 2:
        s = s.join(sys.argv[1])
    elif len(sys.argv) > 2:
        s = s.join(sys.argv[1:])
    morse_code = mt.translate_to_morse(s)
    print(morse_code)


if __name__ == '__main__':
    main()