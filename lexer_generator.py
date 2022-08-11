class JLex:
    class Rule:
        def __init__(self, regex, resulting_type, value_conversion_method=None):
            self.regex = regex
            self.resulting_type = resulting_type
            self.value_conversion_method = value_conversion_method

        def __repr__(self) -> str:
            string = f"Rule - regex: '{self.regex}' resulting type: '{self.resulting_type}'"
            if self.value_conversion_method: 
                string += f" '{self.value_conversion_method}()'"
            return string

    class Lexer:
        def __init__(self, rules):
            self.rules = rules

        def generate_tokens():
            pass

        def print_rules(self):
            if len(self.rules) == 0:
                print("There are no rules.")

            for i in range(len(self.rules)):
                print(f'{i+1}:', self.rules[i])

        def __repr__(self) -> str:
            return f"Lexer{self.rules}"



    #####################################################################

    def __init__(self):
        self.rules = []

    def create_rule(self, regex:str, resulting_type:str, value_conversion_method=None):
        self.rules.append(self.Rule(regex, resulting_type, value_conversion_method))

    def get_rules(self):
        return self.rules

    def print_rules(self):
        if len(self.rules) == 0:
            print("There are no rules.")

        for i in range(len(self.rules)):
            print(f'{i+1}:', self.rules[i])

    def generate_lexer(self):
        if len(self.rules) == 0:
            raise Exception('No rules have been created. Cannot generate lexer.')

        return self.Lexer(self.rules)

if __name__ == "__main__":
   print("JLex executed when ran directly.")
else:
   print("JLex module imported.")

        

