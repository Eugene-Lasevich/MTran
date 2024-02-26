def tokenize_without_regex(input_string):
    operators = {
        "arithmetic": {"+", "-", "*", "/", "%"},
        "assignment": {"=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>="},
        "comparison": {"==", "!=", "<", ">", "<=", ">="},
        "logical": {"&&", "||", "!"},
        "bitwise": {"&", "|", "^", "~", "<<", ">>"},
        "ternary": {"?:", "?."},
        "other": {"::", "..", "!!", "@"}
    }
    keywords = {"var", "val", "Int", "String", "Double", "Boolean", "Byte", "Short", "Long", "Float", "Char", "=", ":"}
    tokens = []
    current_token = ''
    i = 0
    while i < len(input_string):
        char = input_string[i]
        if char == '/':  # Проверяем начало комментария
            if i + 1 < len(input_string) and input_string[i + 1] == '/':
                break  # Если начало комментария, прерываем обработку строки
        if char.isspace():
            if current_token:
                tokens.append(current_token)
                current_token = ''
            i += 1
        elif any(input_string[i:i + len(op)] in op_set for op_set in operators.values() for op in op_set):
            if current_token:
                tokens.append(current_token)
            current_token = input_string[i:i + 2] if input_string[i:i + 2] in operators["ternary"] or input_string[
                                                                                                      i:i + 2] == "->" else char
            if input_string[i:i + 2] in operators["comparison"] or input_string[i:i + 2] in operators["logical"]:
                current_token = input_string[i:i + 2]
                i += 1
            tokens.append(current_token)
            current_token = ''
            i += 2 if input_string[i:i + 2] in operators["ternary"] or input_string[i:i + 2] == "->" else 1
        elif char == ":":
            if current_token:
                tokens.append(current_token)
            current_token = char
            tokens.append(current_token)
            current_token = ''
            i += 1
        else:
            current_token += char
            i += 1
    if current_token:
        tokens.append(current_token)
    return ' '.join(tokens)


def fixed_file():
    input_file_path = "test.kt"
    output_file_path = "corrected_test.kt"
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            corrected_line = tokenize_without_regex(line)
            output_file.write(corrected_line + '\n')

fixed_file()
