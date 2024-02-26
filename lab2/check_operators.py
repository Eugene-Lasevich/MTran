def check_lexical_errors(filename):
    errors = []
    has_errors = False
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if 'if' in line:
                index = line.find('(')
                if index != -1:
                    condition = line[index+1:line.find(')', index)]
                    tokens = condition.split()
                    for token in tokens:
                        if token.strip() == '=':
                            errors.append((i+1, line.strip()))
                            has_errors = True
                            break
            elif 'while' in line:
                index = line.find('(')
                if index != -1:
                    condition = line[index+1:line.find(')', index)]
                    tokens = condition.split()
                    for token in tokens:
                        if token.strip() == '=':
                            errors.append((i+1, line.strip()))
                            has_errors = True
                            break

    if has_errors:
        for error in errors:
            print(f"Ошибка использования оператора на строке {error[0]}: {error[1]}")
    return has_errors
