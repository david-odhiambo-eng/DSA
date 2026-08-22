

class UpperCase:
    def __init__(self, text: str):
        self.text = text

    def upper(self):
        uppercase = ''
        letters_dict = {
            'a': 'A',
            'b': 'B',
            'c': 'C',
            'd': 'D',
            'e': 'E',
            'f': 'F',
            'g': 'G',
            'h': 'H',
            'i': 'I',
            'j': 'J',
            'k': 'K',
            'l': 'L',
            'm': 'M',
            'n': 'N',
            'o': 'O',
            'p': 'P',
            'q': 'Q',
            'r': 'R',
            's': 'S',
            't': 'T',
            'u': 'U',
            'v': 'V',
            'w': 'W',
            'x': 'X',
            'y': 'Y',
            'z': 'Z'
        }
        for letter in self.text:
            uppercase += letters_dict.get(letter, letter)
        print(uppercase)


uppercase = UpperCase('please subscribe to my youtube channel')
uppercase.upper()







    
