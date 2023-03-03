from lark import Lark, Transformer, Discard

grammar = r"""
start: termo*
termo: cabecalho var* traducao* NEWLINE

cabecalho: "# " ID ": " PALAVRA SEP PALAVRA SEP TIPO NEWLINE
var: TIPO " - " ANY NEWLINE
traducao: linguagem ": " PALAVRA NEWLINE

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


class MyTransformer(Transformer):
    def PALAVRA(self, el):
        return el.strip()

    def SEP(self, _):
        return Discard

    def NEWLINE(self, _):
        return Discard

    def cabecalho(self, el):
        id = el[0].value
        palavra = el[1]
        area = el[2]
        tipo = el[3].value
        return {"id": id, "palavra": palavra, "area": area, "tipo": tipo}

    def linguagem(self, el):
        if len(el) == 1:
            return (el[0].value, None)
        else:
            return (el[0].value, el[1].value)

    def termo(self, el):
        head = el[0]
        vars = {}
        terms = []
        for e in el[1:]:
            if e.data == "var":
                vars[e.children[0].value] = e.children[1].value
            elif e.data == "traducao":
                terms.append((e.children[0], e.children[1]))
        terms.append((("gl", None), head["palavra"]))
        return {
            "id": head["id"],
            "area": head["area"],
            "type": head["tipo"],
            "terms": terms,
            "vars": vars,
        }


parser = Lark(grammar)
tree = parser.parse(open("exemplo.txt").read())

print("PARSED:")
print(MyTransformer().transform(tree))
