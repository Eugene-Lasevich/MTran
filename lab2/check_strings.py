def read_code_from_file(filename):
    with open(filename, 'r') as file:
        code = file.readlines()
    return code

def are_quotes_closed(line):
    stack = []
    for i, char in enumerate(line):
        if char == '"':
            if stack and stack[-1][0] == '"':
                stack.pop()
            else:
                stack.append(('"', i))
        elif char == "'":
            if stack and stack[-1][0] == "'":
                stack.pop()
            else:
                stack.append(("'", i))
    if stack:
        return False, stack[-1][1]  # Возвращаем False и позицию символа в строке
    return True, None

def check_quotes(filename):
    code = read_code_from_file(filename)
    has_errors = False
    for line_number, line in enumerate(code, 1):
        result, error_position = are_quotes_closed(line)
        if not result:
            print("Ошибка: Незакрытые кавычки в строке {} файла {}".format(line_number, filename))
            has_errors = True
            break
    if not has_errors:
        pass
    return has_errors

