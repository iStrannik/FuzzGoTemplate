from antlr4 import *
from count_lexer import count_lexer
from count_parserListener import count_parserListener
from count_parser import count_parser
import sys

def main():
    lexer = count_lexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = count_parser(stream)
    tree = parser.start()
    printer = count_parserListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()