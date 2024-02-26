import sys
def read_code_from_file(filename):
    with open(filename, 'r') as file:
        code = file.readlines()
    return code

def find_typo_in_keywords(code):
    keywords = ['if', 'else', 'while', 'for', 'when', 'return', 'fun', 'class', 'interface', 'object', 'package', 'import', 'val', 'var']
    for line_number, line in enumerate(code, 1):
        words = line.split()
        for word in words:
            if word not in keywords:
                min_diff = float('inf')
                closest_keyword = None
                for keyword in keywords:
                    if len(word) == len(keyword):
                        diff_count = sum(c1 != c2 for c1, c2 in zip(word, keyword))
                        if diff_count < min_diff:
                            min_diff = diff_count
                            closest_keyword = keyword
                if min_diff == 1:
                    return line_number, word, closest_keyword
    return None

def print_error(error_type, error):
    if error:
        line_number, word, closest_keyword = error
        print("Обнаружена лексическая ошибка типа '{}' в строке {}: {}, ближайшее ключевое слово: {}".format(error_type, line_number, word, closest_keyword))
        sys.exit(0)


