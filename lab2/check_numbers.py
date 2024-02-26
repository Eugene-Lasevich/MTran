def is_valid_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False

def check_numbers_in_lines(lines):
    has_errors = False
    for i, line in enumerate(lines, 1):
        line = line.strip()
        if line.startswith("var") or line.startswith("val"):
            equal_sign_index = line.find('=')
            if equal_sign_index != -1:
                variable, value = line[:equal_sign_index].strip(), line[equal_sign_index + 1:].strip()
                if not any(keyword in value for keyword in {"if", "else", "for", "while", "do", "when", "return", "println", "readLine", "true", "false"}):
                    if not value.startswith('"') and not is_valid_number(value):
                        print(f"Ошибка в написании числа {i}: {line}")
                        has_errors = True
    return has_errors

def main():
    filename = "test.kt"
    with open(filename, 'r', encoding="UTF-8") as file:
        lines = file.readlines()
    has_errors = check_numbers_in_lines(lines)
    if not has_errors:
        print("Лексические ошибки не найдены.")


