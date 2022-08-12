import re


class JLex:
    
    #####################################################################
    class Rule:
        def __init__(self, regex, resulting_type, value_conversion_method=None):
            self.regex = regex
            self.resulting_type = resulting_type
            self.value_conversion_method = value_conversion_method

        def __repr__(self) -> str:
            string = f"Rule <regex: '{self.regex}', resulting type: '{self.resulting_type}'>"
            if self.value_conversion_method: 
                string += f" '{self.value_conversion_method}()'"
            return string

    #####################################################################

    class Lexer:
        ####################################
        class Token:
            def __init__(self, type, value):
                self.type = type
                self.value = value

            def __repr__(self) -> str:
                return f"(Token - type: '{self.type}', value: '{self.value}')"
        ####################################

        def __init__(self, rules):
            self.rules = rules

        def match_rules(self, input:str):
            for rule in self.rules:
                match = re.match(rule.regex, input)
                if match:
                    value = match.group(0)
                    return self.Token(rule.resulting_type, value), len(value)

            raise Exception('No matches.')

        def generate_tokens(self, input:str):
            if len(input) == 0:
                raise Exception('Input string is empty.')

            token_list = []
            while len(input) > 0:
                token, consumed_chars = self.match_rules(input)
                token_list.append(token)
                input = input[consumed_chars:len(input)]

            return token_list

        def __repr__(self) -> str:
            string = "Lexer<"
            num_rules = len(self.rules)
            string += f"\n\tNumber of rules: {num_rules}\n"
            for i in range(num_rules):
                string += f'\t{i+1}: {self.rules[i]}'
                if i < num_rules:
                    string += '\n'

            string += ">"
            return string

    #####################################################################

    def __init__(self):
        self.rules = []

    def create_rule(self, regex:str, resulting_type:str, value_conversion_method=None):
        self.rules.append(self.Rule(regex, resulting_type, value_conversion_method))
        return self

    def get_rules(self):
        return self.rules

    def print_rules(self):
        if len(self.rules) == 0:
            print("There are no rules.")

        string = ''
        for i in range(len(self.rules)):
            string += f'{i+1}: {self.rules[i]}\n'
        print(string)

    def generate_lexer(self):
        if len(self.rules) == 0:
            raise Exception('No rules have been created. Cannot generate lexer.')

        return self.Lexer(self.rules)

if __name__ == "__main__":
   print("JLex executed when ran directly.")
else:
   print("JLex module successfully imported.")
