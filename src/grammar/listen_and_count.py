from antlr4 import *

from .count_lexer import count_lexer
from .count_parser import count_parser
from .count_parserListener import count_parserListener


def listen_and_count(tpl):
    lexer = count_lexer(InputStream(tpl))
    stream = CommonTokenStream(lexer)
    parser = count_parser(stream)
    tree = parser.start()
    printer = count_parserListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
