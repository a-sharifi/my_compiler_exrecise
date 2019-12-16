import sys
from antlr4 import *
from ArrayLexer import ArrayLexer
from ArrayParser import ArrayParser
from ArrayListener import ArrayListener

class ArrayPrintListener(ArrayListener):
    def enterR(self,ctx):
        print("Array {}".format(ctx.ID()))

def main(argv):
    _input = FileStream('/Users/amir/PycharmProjects/my_compiler_exrecise/antlr/test.pp')
    lexer = ArrayLexer(_input)
    stream = CommonTokenStream(lexer)
    parser = ArrayParser(stream)
    tree = parser.type()
    printer = ArrayPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer,tree)
    print('Done with no error')

    # parser.addContextToParseTree()
 
if __name__ == '__main__':
    main(sys.argv)
