from string import digits, ascii_lowercase, ascii_uppercase, whitespace, punctuation
from logging import error
import argparse
import json 

class LexicalError(Exception):
    pass


class Scanner:
    def __init__(self):
        self.state = 0
        self.look_ahead = 0
        self._relop = ['<', '>', '=']
        self._punctuations = {
            '(': 'OPEN_PRENTHESIS',
            ')': 'CLOSE_PRENTHESIS',
            '[': 'OPEN_BRACKET',
            ']': 'CLOSE_BRACKET',
            '{': 'OPEN_CURLY_PRENTHESIS',
            '}': 'CLOSE_CURLY_PRENTHESIS'
        }
        self._keywords = {
            'if':     'IF',
            'else':   'ELSE',
            'return': 'RETURN',
            'while':  'WHILE',
            'then':   'THEN',
            'of':     'OF',
            'array':  'ARRAY',
            'char' : 'CHAR',
            'integer' : 'INTEGER'
        }
        self._id = ''
        self._digit = ''
        self._line_number = 1

    def code_to_char(self, code):
        pass

    def _next_char(self):
        try:
            self.look_ahead += 1
            char = self._chars[self.look_ahead]
            return char
        except IndexError:
            return None

    def current_char(self):
        return self._chars[self.look_ahead]

    def scanner(self, input_code):
        self._chars = list(input_code)

        while not (self.look_ahead == len(self._chars)):

            if self.state == 0:
                char = self.current_char()
                self._id = ''
                self._digit = ''
                self._punctuation = ''
                # self._line_number = ''
                if char == '<':
                    self.state = 1

                elif char == '>':
                    self.state = 6

                elif char == '=':
                    self.state = 5

                elif char in (ascii_lowercase + ascii_uppercase):
                    self._id += char
                    self.state = 9

                elif char in digits:
                    self._digit += char
                    self.state = 11

                elif char in whitespace:
                    if char == '\n':
                        self._line_number += 1
                    self.look_ahead += 1

                elif char in self._punctuations:
                    self._punctuation += char
                    self.state = 20

                elif char == '.':
                    self.state = 21

                else:
                    raise LexicalError("In Line {}".format(self._line_number))
            elif self.state == 1:
                char = self._next_char()

                if char == '=':
                    self.state = 2

                elif char == '>':
                    self.state = 3

                elif char not in ['=', '>']:
                    self.state = 4

            # '<=' Less Equal
            elif self.state == 2:
                char = self._next_char()
                self.state = 0
                yield ('relop', 'LE')

            # '<>' Not Equal
            elif self.state == 3:
                char = self._next_char()
                self.state = 0
                yield ('relop', 'NE')

            # '<' Less Than
            elif self.state == 4:
                # get one more useless char in the state 1 and dont need LA go next
                self.state = 0
                yield('relop', 'LT')

            # '=' Equal
            elif self.state == 5:
                self.state = 0
                char = self._next_char()
                yield ('relop', 'EQ')

            elif self.state == 6:
                char = self._next_char()
                if char == '=':
                    self.state = 7
                elif char not in ['=']:
                    self.state = 8

            # '>=' Greater equal
            elif self.state == 7:
                char = self._next_char()
                self.state = 0
                yield ('relop', 'GE')

            # '>' Greater than
            elif self.state == 8:
                # get one more useless char in the state 1 and dont need to call LA go next
                self.state = 0
                yield ('relop', 'GT')

            # Detect IDs
            elif self.state == 9:
                char = self._next_char()

                if char in ascii_lowercase + ascii_uppercase + digits:
                    self._id += char
                    self.state = 9

                else:
                    self.state = 10

            elif self.state == 10:
                # get one more useless char in the state 1 and dont need to call LA go next
                self.state = 0
                try:
                    yield ('keyword', self._keywords[self._id])

                except KeyError:
                    yield('id','ID',self._id)

            elif self.state == 11:
                char = self._next_char()
                if char in digits:
                    self.state = 11
                    self._digit += char
                if char == '.':
                    self.state = 12
                    self._digit += char
                elif char not in digits + '.':
                    self.state = 18

            elif self.state == 12:
                char = self._next_char()
                if char in digits:
                    self._digit += char
                    self.state = 13

            elif self.state == 13:
                char = self._next_char()

                if char in digits:
                    self.state = 13
                    self._digit += char

                elif char not in digits + 'Ee':
                    self.state = 19

                elif char in 'Ee':
                    self.state = 14
                    self._digit += char

            elif self.state == 14:
                char = self._next_char()

                if char in '+-':
                    self.state = 15
                    self._digit += char

                elif char in digits:
                    self.state = 16
                    self._digit += char

            elif self.state == 15:
                char = self._next_char()
                if char in digits:
                    self.state = 16
                    self._digit += char

            elif self.state == 16:
                char = self._next_char()

                if char in digits:
                    self.state = 16
                    self._digit += char

                elif char not in digits:
                    self.state = 17

            elif self.state == 17:
                # get one more useless char in the state 1 and dont need to call LA go next
                self.state = 0
                yield ('digit','DIGIT', self._digit)

            # Detect Int digit
            elif self.state == 18:
                # get one more useless char in the state 1 and dont need to call LA go next
                self.state = 0
                yield ('digit','DIGIT', self._digit)

            # Detect Float digit
            elif self.state == 19:
                # get one more useless char in the state 1 and dont need to call LA go next
                self.state = 0
                yield ('digit','DIGIT', self._digit)

            # Detect Punctuation
            elif self.state == 20:
                self._next_char()
                self.state = 0
                yield ('punctuation', self._punctuations[self._punctuation])

            elif self.state == 21:
                char = self._next_char()
                if char == '.':
                    self.state = 22

            elif self.state == 22:
                self._next_char()
                self.state = 0
                yield('dotdot', 'DOTDOT')

def main():
    ap = argparse.ArgumentParser()

    ap.add_argument("-i", "--input", required=False, default='test.amir',
                help="path to input source code file")

    ap.add_argument("-o", "--output", required=False, default='out.txt',
                help="path to output lexical analyzer.txt")

    args = vars(ap.parse_args())

    with open(args['input']) as f:
        code = f.read()

    
    try:
        handler = Scanner()
        lex = list(handler.scanner(
            code))
        with open(args['output'],'w') as f:
            json.dump(lex, f)
    except LexicalError as err:
        error('Lexical error occured {}'.format(err))



if __name__ == "__main__":

    main()