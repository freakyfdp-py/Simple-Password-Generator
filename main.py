import random, string, json, typing

def load_config() -> list[int, int, str, str, str, str]:
    password_length = int(input('Enter the length of the password >> '))
    password_count = int(input('How many password to generate >> '))
    use_lowercase = input('Use lowercase ( y/n ) >>')
    use_uppercase = input('Use uppercase ( y/n ) >>')
    use_symbols = input('Use symbols ( y/n ) >>')
    use_digits = input('Use digits ( y/n ) >>')
    print('\n', end='')

    return password_length, password_count, use_lowercase, use_uppercase, use_symbols, use_digits
    
def get_allowed_characters(use_lowercase, use_uppercase, use_symbols, use_digits) -> str:
    allowed_characters = ''
    
    if use_lowercase == 'y':
        allowed_characters += string.ascii_lowercase
    if use_uppercase == 'y':
        allowed_characters += string.ascii_uppercase
    if use_symbols == 'y':
        allowed_characters += string.punctuation
    if use_digits == 'y':
        allowed_characters += string.digits

    return allowed_characters

def generate_password(password_length, use_lowercase, use_uppercase, use_symbols, use_digits) -> str:
    allowed_characters = get_allowed_characters(use_lowercase, use_uppercase, use_symbols, use_digits)
    
    return ''.join(random.choices(allowed_characters, k=password_length))

def main() -> None:
    password_length, password_count, use_lowercase, use_uppercase, use_symbols, use_digits = load_config()

    for i in range(password_count):
        password = generate_password(password_length, use_lowercase, use_uppercase, use_symbols, use_digits)
        print(password + '\n', end='')

if __name__ == '__main__':
    main()