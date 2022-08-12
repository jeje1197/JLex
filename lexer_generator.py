import re
import types


class JLex:
    
    #####################################################################
    class Rule:
        def __init__(self, regex, result_type, value_conversion_method=None):
            self.regex = regex
            self.result_type = result_type
            self.conversion_method = value_conversion_method

        def __repr__(self) -> str:
            string = f"Rule <regex: '{self.regex}', result type: '{self.result_type}'>"
            if self.conversion_method: 
                string += f" conversion method: '{self.conversion_method.__name__}()'"
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

        def __init__(self, rules, skip_rules=None):
            self.rules = rules
            self.skip_rules = skip_rules

        def match_rules(self, input:str):
            for rule in self.skip_rules:
                match = re.match(rule.regex, input)
                if match:
                    value = match.group(0)
                    consumed_chars = len(value)
                    return None, consumed_chars

            for rule in self.rules:
                match = re.match(rule.regex, input)
                if match:
                    value = match.group(0)
                    consumed_chars = len(value)
                    if isinstance(rule.conversion_method, types.FunctionType):
                        value = rule.conversion_method(value)
                    return self.Token(rule.result_type, value), consumed_chars

            raise Exception(f'No matches: "{input}"')


        def generate_tokens(self, input:str):
            if len(input) == 0:
                raise Exception('Input string is empty.')

            token_list = []
            while len(input) > 0:
                print(input)
                token, consumed_chars = self.match_rules(input)
                if token:
                    token_list.append(token)
                input = input[consumed_chars:len(input)]

            return token_list

        def __repr__(self) -> str:
            string = "Lexer<"
            num_rules = len(self.rules)
            num_skip_rules = len(self.skip_rules)
            string += f"\n\tNumber of rules: {num_rules}\n"
            for i in range(num_rules):
                string += f'\t{i + 1}: {self.rules[i]}'
                if i < num_rules:
                    string += '\n'

            string += f"\n\tNumber of skip rules: {num_skip_rules}\n"
            for i in range(num_skip_rules):
                string += f'\t{num_rules + i + 1}: {self.skip_rules[i]}'
                if i < num_skip_rules:
                    string += '\n'

            string += ">"
            return string

    #####################################################################

    def __init__(self):
        self.rules = []
        self.skip_rules = []

    def create_rule(self, regex:str, resulting_type:str, value_conversion_method=None):
        self.rules.append(self.Rule(regex, resulting_type, value_conversion_method))
        return self

    def create_rules_from_list(self, list:list):
        if len(list) == 0:
            raise Exception("Passed in empty list.")

        for tuple in list:
            if not len(tuple) in (2, 3):
                raise Exception("Expected tuples with 2 or 3 values. Ex. tuple = (regex, result_type, optional:conversion_method).")

            regex = tuple[0]
            result_type = tuple[1]
            conversion_method = tuple[2] if len(tuple) == 3 else None

            self.rules.append(self.Rule(regex, result_type, conversion_method))

    def create_skip_rule(self, regex:str):
        self.skip_rules.append(self.Rule(regex, None, None))
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

        return self.Lexer(self.rules, self.skip_rules)


if __name__ == "__main__":
   print("JLex executed when ran directly.")
else:
   print("JLex module successfully imported.")
