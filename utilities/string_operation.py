def reverse_string(text):
    return text[::-1]


def capitalize_string(text):
    return text.capitalize()


def lowercase_string(text):
    return text.lower()


def uppercase_string(text):
    return text.upper()


if __name__ == '__main__':
    sample = 'Hello World'
    print('reverse_string:', reverse_string(sample))
    print('capitalize_string:', capitalize_string(sample))
    print('lowercase_string:', lowercase_string(sample))
    print('uppercase_string:', uppercase_string(sample))
