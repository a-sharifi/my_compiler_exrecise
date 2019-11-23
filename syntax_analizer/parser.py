
import json
from logging import error
import argparse


'''
TYPES KEYS:
relop
keyword
id
digit
punctuation
dotdot

lookahead('type','VALUE')
'''


class Parser:
    def __init__(self, parsed_lex):
        self._parsed_lex = parsed_lex
        self._lookahead = parsed_lex[0]
        self._index = 0

    def _next_token(self):
        self._index += 1
        return self._parsed_lex[self._index]

    def _match(self, token):
        if self._lookahead[1] == token:
            self._lookahead = self._next_token()

        else:
            raise SyntaxError

    def _simple(self):
        if self._lookahead[0] == 'keyword' and self._lookahead[1] == 'INTEGER':
            self._match('INTEGER')

        elif self._lookahead[0] == 'keyword' and self._lookahead[1] == 'CHAR':
            self._match('CHAR')

        elif self._lookahead[1] == 'DIGIT':
            self._match('DIGIT')
            self._match('DOTDOT')
            self._match('DIGIT')
        
        else:
            raise SyntaxError
    
    def _type(self):
    
        if self._lookahead[1] in ('INTEGER','CHAR','DIGIT'):
            self._simple()
            print('1')

        elif self._lookahead[1] == 'ID':
            self._match('ID')
            print('2')
            
        elif self._lookahead[1] == 'ARRAY':
            self._match('ARRAY')
            self._match('OPEN_BRACKET')
            self._simple()
            self._match('CLOSE_BRACKET')
            self._match('OF')
            self._type()
            print('3')

        else:
            raise SyntaxError

    def run(self):
        try:
            while True:
                self._type()
        except IndexError as err:
            print('No Syntax Error')
            

def load_lexical_analyzed_file(file):
    with open(file) as f:
        loaded_file = json.load(f)
    return loaded_file


if __name__ == "__main__":
    ap = argparse.ArgumentParser()

    ap.add_argument("-i", "--input", required=False, default='out.txt',
                help="path to input source code file")

    args = vars(ap.parse_args())
    input_lex = load_lexical_analyzed_file(args['input'])
    parser = Parser(input_lex)
    parser.run()
