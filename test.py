import re
from lexer_generator import JLex

# Create JLex Object
jlex = JLex()

# Create rules for lexer
# jlex.create_rule("\+", "PLUS")
# jlex.create_rule("\-", "MINUS")
# jlex.create_rule("\*", "MUL")
# jlex.create_rule("/", "DIV")
# jlex.create_rule("\d*\.\d+", "FLOAT")
# jlex.create_rule("\d+", "INT")

def string_formatter(string:str):
    return string.replace('"', '').replace("\\n", "\n").replace("\\t", "\t")

# print("Test Newline_formatter:", newline_formatter("\\n1\\n2\\n3"))

# Rules should be listed in order of desired execution
jlex.create_rules_from_list([
    # (regex, classification, optional:conversion_method)
    ("[\n;]", "NEWLINE"),
    ("\"[(.)*?\n*?]\"", "STRING", string_formatter),
    ("\+{2}", "INCREMENT"),
    ("\+", "PLUS"),
    ("\-{2}", "DECREMENT"),
    ("\-", "MINUS"),
    ("\*", "MUL"),
    ("/", "DIV"),
    ("\^", "POW"),
    ("%", "MOD"),
    ("!", "NOT"),
    ("!=", "NE"),
    ("==", "EE"),
    ("<", "LT"),
    ("<=", "LTE"),
    (">", "GT"),
    (">=", "GTE"),
    ("\d*\.\d+", "FLOAT"),
    ("\d+", "INT"),
])

jlex.create_skip_rule("[\t ]*")


# Create lexer object
lexer = jlex.generate_lexer()
print(f"-----Generated Lexer-----\n{lexer}")

# Generate list of tokens from string
# test_input = '++1+++2*3/4.0-8"String 1"'
# tokens = lexer.generate_tokens(test_input)
# print("-----List of Generated Tokens-----")
# for token in tokens:
#     print(token)