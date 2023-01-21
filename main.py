from antlr4 import *
from gen.nlanVisitor import nlanVisitor
from gen.nlanLexer import nlanLexer
from gen.nlanParser import nlanParser


def main():
    file = input("Write file name: ")
    with open(file, "r") as file:
        input_str = file.read()
    data = InputStream(input_str)
    lexer = nlanLexer(data)
    stream = CommonTokenStream(lexer)
    parser = nlanParser(stream)
    tree = parser.program()
    visitor = nlanVisitor()
    output = visitor.visit(tree)


if __name__ == '__main__':
    main()
