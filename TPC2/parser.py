from lark import Lark

grammar = r"""
start: termo*
termo: cabecalho nota* traducao* NEWLINE

cabecalho: "# " ID ": " PALAVRA SEP area SEP TIPO NEWLINE
nota: /\w+/ " - " ANY NEWLINE
traducao: linguagem ": " PALAVRA NEWLINE

area: PALAVRA
TIPO: /\w+/
linguagem: LINGUAGEM (" " PAIS)?

PAIS: /\[\w\w\]/
LINGUAGEM: /[a-z][a-z]/
PALAVRA: /[^|\n]+/
ANY: /.+/
NEWLINE: /\n/
SEP: "| "

ID: /[0-9]+/
"""

parser = Lark(grammar)
print(parser.parse(open("exemplo.txt").read()).pretty())
