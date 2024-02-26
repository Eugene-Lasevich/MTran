def check_variable_naming_errors(filename):
    has_errors = False
    digit_start_errors = []
    hyphen_errors = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            words = line.split()
            for j, word in enumerate(words):
                if word in ['var', 'val'] and j < len(words) - 1:
                    next_word = words[j + 1]
                    if next_word[0].isdigit():
                        has_errors = True
                        digit_start_errors.append((i + 1, next_word))
                    elif '-' in next_word:
                        has_errors = True
                        hyphen_errors.append((i + 1, next_word))
    return has_errors, digit_start_errors, hyphen_errors


def print_errors(has_errors, digit_start_errors, hyphen_errors):
    if has_errors:
        print("Обнаружены ошибки в именовании переменных:")
        if digit_start_errors:
            print("Ошибки: Переменные начинаются с цифры:")
            for error in digit_start_errors:
                print(f"Ошибка на строке {error[0]}: Переменная '{error[1]}' начинается с цифры.")
        if hyphen_errors:
            print("\nОшибки: Переменные содержат '-':")
            for error in hyphen_errors:
                print(f"Ошибка на строке {error[0]}: Переменная '{error[1]}' содержит '-'.")

    else:
        pass



