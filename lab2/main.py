import sys
import check_numbers
import check_keywords
import check_operators
import check_strings
from check_variables import *
from fix_file import *


class Lexer:
    def __init__(self):
        self.keywords = {
            "control": {"if", "else", "for", "while", "do", "return", "continue", "break", "when", "in", "is", "as",
                        "println", "readLine"},
            "modifiers": {"var", "val", "fun", "package", "import"},
            "types": {"Boolean", "Byte", "Char", "Double", "Float", "Int", "Long", "Short", "String", "Any", "Unit"},
            "miscellaneous": {"true", "false", "null", "throw", "try", "catch", "finally", "object", "typealias"}
        }
        self.operators = {
            "arithmetic": {"+", "-", "*", "/", "%"},
            "assignment": {"=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>="},
            "comparison": {"==", "!=", "<", ">", "<=", ">="},
            "logical": {"&&", "||", "!"},
            "bitwise": {"&", "|", "^", "~", "<<", ">>"},
            "ternary": {"?:", "?."},
            "other": {"::", "->", "..", "!!", "@"}
        }
        self.symbols = {'(', ')', '{', '}', ':', ',', ';', '.', '[', ']', '?', '->', '?:', '?'}

    def analyze(self, input_code):
        token_table = []
        identifier_table = []
        keyword_table = set()
        operator_table = set()
        in_string = False
        id_counter = 1
        identifiers = {}  # Словарь для отслеживания идентификаторов и их типов
        for line in input_code:
            tokens = []
            current_token = ''
            for char in line.strip():
                if char == '"':
                    in_string = not in_string
                    if in_string:
                        current_token += char
                    else:
                        current_token += char
                        tokens.append(current_token)
                        current_token = ''
                elif char == ' ' and not in_string:
                    if current_token:
                        tokens.append(current_token)
                        current_token = ''
                elif char in {'(', ')'}:
                    if current_token:
                        tokens.append(current_token)
                        current_token = ''
                    tokens.append(char)
                else:
                    current_token += char
            if current_token:
                tokens.append(current_token)

            processed_tokens, id_counter = self.process_tokens(tokens, in_string, id_counter, identifiers)
            token_table.extend(processed_tokens)
            identifier_table.extend(
                [(token_type, token_value, token_info) for token_type, token_value, token_info in processed_tokens if
                 token_type == "Identifier"])

            # Заполнение таблиц ключевых слов и операторов
            for token_type, token_value, token_info in processed_tokens:
                if token_type.startswith("Keyword"):
                    keyword_table.add(token_value)
                elif token_type.startswith("Operator"):
                    operator_table.add(token_value)

        return token_table, identifier_table, keyword_table, operator_table

    def process_tokens(self, tokens, in_string, id_counter, identifiers):
        processed_tokens = []
        is_variable_declaration = False  # Флаг для отслеживания объявления переменной

        for token in tokens:
            if in_string:
                processed_tokens.append(("String", token, ""))
            elif token in self.keywords["control"]:
                processed_tokens.append(("Keyword (control)", token, ""))
                is_variable_declaration = False  # Сбрасываем флаг при встрече ключевого слова
            elif token in self.keywords["modifiers"]:
                processed_tokens.append(("Keyword (modifiers)", token, ""))
                is_variable_declaration = True  # Устанавливаем флаг при встрече модификатора
            elif token in self.keywords["types"]:
                processed_tokens.append(("Keyword (types)", token, ""))
            elif token in self.keywords["miscellaneous"]:
                processed_tokens.append(("Keyword (miscellaneous)", token, ""))
                is_variable_declaration = False  # Сбрасываем флаг при встрече ключевого слова
            elif token in self.operators["arithmetic"]:
                processed_tokens.append(("Operator (arithmetic)", token, ""))
                is_variable_declaration = False  # Сбрасываем флаг при встрече оператора
            elif token in self.operators["assignment"]:
                processed_tokens.append(("Operator (assignment)", token, ""))
                is_variable_declaration = False  # Сбрасываем флаг при встрече оператора
            elif token in self.operators["comparison"]:
                processed_tokens.append(("Operator (comparison)", token, ""))
                is_variable_declaration = False  # Сбрасываем флаг при встрече оператора
            elif token in self.operators["logical"]:
                processed_tokens.append(("Operator (logical)", token, ""))
                is_variable_declaration = False  # Сбрасываем флаг при встрече оператора
            elif token in self.operators["bitwise"]:
                processed_tokens.append(("Operator (bitwise)", token, ""))
                is_variable_declaration = False  # Сбрасываем флаг при встрече оператора
            elif token in self.operators["ternary"]:
                processed_tokens.append(("Operator (ternary)", token, ""))
                is_variable_declaration = False  # Сбрасываем флаг при встрече оператора
            elif token in self.operators["other"]:
                processed_tokens.append(("Operator (other)", token, ""))
                is_variable_declaration = False  # Сбрасываем флаг при встрече оператора
            elif token in self.symbols:
                processed_tokens.append(("Symbol", token, ""))
                is_variable_declaration = False  # Сбрасываем флаг при встрече символа
            else:
                # Если это идентификатор, проверяем, был ли он уже встречен ранее
                if token in identifiers:
                    # Если да, используем тот же тип
                    processed_tokens.append((identifiers[token], token, ""))
                else:
                    # Иначе, добавляем новый идентификатор и определяем его тип
                    if is_variable_declaration:
                        # Если идентификатор в контексте объявления переменной, он является переменной
                        identifiers[token] = "Identifier"
                        token_info = "Variable"
                    else:
                        # Иначе он является константой
                        identifiers[token] = "Constant"
                        token_info = "Constant"
                    processed_tokens.append(("Identifier", token, token_info))
                    id_counter += 1

        return processed_tokens, id_counter


def print_table(title, data):
    print(f"{title}:")
    for index, item in enumerate(data, 1):
        print(f"{index}: {item}")


def print_tokens(token_table):
    for index, token_info in enumerate(token_table, 1):
        print(f"Token {index}: {token_info}")


from collections import OrderedDict


def print_identifiers(identifier_table):
    unique_identifiers = OrderedDict()

    for index, (token_type, token_value, token_info) in enumerate(identifier_table, 1):
        if token_value not in unique_identifiers:
            unique_identifiers[token_value] = token_info

    for index, (identifier, info) in enumerate(unique_identifiers.items(), 1):
        print(f"Identifier ({index}): {identifier} ({info})")


def main():
    lexer = Lexer()
    filename = "corrected_test.kt"
    with open(filename, 'r', encoding="UTF-8") as file:
        input_code = file.readlines()
    token_table, identifier_table, keyword_table, operator_table = lexer.analyze(input_code)

    print("All tokens:")
    print_tokens(token_table)
    # print_table("Identifier Table", identifier_table)
    print_identifiers(identifier_table)
    print()
    print_table("Keyword Table", keyword_table)
    print()
    print_table("Operator Table", operator_table)


if __name__ == "__main__":
    filename = "test.kt"
    has_errors, digit_start_errors, hyphen_errors = check_variable_naming_errors(filename)
    print_errors(has_errors, digit_start_errors, hyphen_errors)
    if check_strings.check_quotes(filename):
        sys.exit(0)
    if has_errors:
        sys.exit(0)
    with open(filename, 'r', encoding="UTF-8") as file:
        lines = file.readlines()
    has_errors = check_numbers.check_numbers_in_lines(lines)
    if has_errors:
        sys.exit(0)
    fixed_file()
    filename = "corrected_test.kt"
    code = check_keywords.read_code_from_file(filename)
    error_type = "опечатка в ключевом слове"
    error = check_keywords.find_typo_in_keywords(code)
    if check_keywords.print_error(error_type, error):
        sys.exit(0)
    if check_operators.check_lexical_errors(filename):
        sys.exit(0)

    main()
