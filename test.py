from lexer_generator import JLex

jlex = JLex()

jlex.create_rule("\+", "ADD")
jlex.create_rule("\d", "INT")

jlex.print_rules()

lexer = jlex.generate_lexer()
print(lexer)