from antlr4 import *
from generated.WhileLangLexer import WhileLangLexer
from generated.WhileLangParser import WhileLangParser

# === Entrada de prueba ===
input_text = """a = 10;
b = 20;
if (a > b) {
max = a;
} else {
if (a == b) {
    max = a;
} else {
    max = b;
}
}
"""

# Crear flujo de entrada
input_stream = InputStream(input_text)

# === Fase léxica ===
lexer = WhileLangLexer(input_stream)
token_stream = CommonTokenStream(lexer)
token_stream.fill()

print("## 🔤 TOKENS")
for token in token_stream.tokens:
    if token.type != Token.EOF:
        print(f"  - {lexer.symbolicNames[token.type]} ('{token.text}') @line {token.line}:{token.column}")

print("\n## 🌳 ÁRBOL SINTÁCTICO (toStringTree)")
parser = WhileLangParser(token_stream)
tree = parser.program()
print(tree.toStringTree(recog=parser))

# === Representación indentada ===
def pretty_tree(node, rule_names, level=0):
    if isinstance(node, TerminalNode):
        return "  " * level + f"TOKEN({node.getText()})"
    else:
        rule_name = rule_names[node.getRuleIndex()]
        result = "  " * level + rule_name
        for child in node.children or []:
            result += "\n" + pretty_tree(child, rule_names, level + 1)
        return result

print("\n## 🌲 ÁRBOL SINTÁCTICO (Indentado)")
print(pretty_tree(tree, parser.ruleNames))