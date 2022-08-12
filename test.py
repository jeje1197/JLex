from lexer_generator import JLex

jlex = JLex()

# Create rules for lexer
jlex.create_rule("\+", "ADD")
jlex.create_rule("\-", "SUB")
jlex.create_rule("\*", "MUL")
jlex.create_rule("\*", "DIV")
jlex.create_rule("\d+", "INT")
jlex.create_rule("(\d)*.(\d+)", "FLOAT")

# Create lexer object
lexer = jlex.generate_lexer()
print(f"Lexer object:\n{lexer}")

string = "1+2*3/4"
tokens = lexer.generate_tokens(string)
print(tokens)