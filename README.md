# JLex

JLex is lexer generator I created to shorten the process of developing a programming
language. A lexer, also referred to as a tokenizer, is a program that takes in a string
and outputs a list of tokens based on a set of pre-defined rules. A lexer generator is a
program that takes in a list of regular expressions and token types to convert the matches
into then returns a lexer object which you can then use to turn a string into a list of tokens.
Lexer generators are nice because they generate the code to tokenize a string for you.


# lexer_generator.py

This is the source code for the projects. Feel free to examine it to see how it generates rules from
the (regex, token_type) tuples you pass it.

# test.py

This is a test file where I load in some rules and check if the resulting lexer
can produce a list of properly formatted tokens.
