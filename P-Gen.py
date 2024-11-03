import argparse
import os
import itertools
import random
import string

symbols = [".", "-", "_", "?", "!", "@", "#", "+", "*", "%", "&", "$"]
range_21 = range(1, 21)
common_pwds = [
    "password",
    "admin",
    "123456",
    "1234567890",
    "qwerty",
    "qwertyuiop",
    "webadmin",
    "1q2w3e4r5t",
    "qwerty123",
    "11111111",
]

leet_chars = {
    'a': '4', 'b': '8', 'e': '3', 'g': '6',
    'i': '1', 'o': '0', 's': '5', 't': '7',
    'z': '2',

}

directory = "output"
min_pwd_length = 0


def create_output_folder():
    if not os.path.exists(directory):
        os.makedirs(directory)


def create_output_file(input_filename):
    create_output_folder()
    filename = os.path.join(directory, input_filename)

    if os.path.exists(filename):
        choice = input(
            "[!] {} already exists. Do you want to overwrite? (y/n):".format(
                input_filename
            )
        )
        if str(choice).lower() != "y":
            exit(1)
    else:
        open(filename, 'w').close()  # Create an empty file


def prepare_keywords(str_input):
    if not str_input or len(str_input) == 0:
        return None
    temp = str_input.split(",")
    result = [elem.strip() for elem in temp if elem.strip() != ""]
    return result


def create_permutations_with_repetition(list_input, k):
    unique_words = set(list_input)
    subsets = [p for p in itertools.product(unique_words, repeat=k)]
    return subsets


def flush_None_values(list_input):
    return [elem for elem in list_input if elem is not None and elem != ""]


def attr_keywords_in_unique_list(target):
    attributes = vars(target)
    regular_attributes = []
    keyword_lists = []

    for attr in attributes.values():
        if isinstance(attr, list):
            keyword_lists.extend(attr)
        elif attr is not None and attr != "":
            regular_attributes.append(attr)

    result = list(set(regular_attributes))
    result.extend(keyword_lists)
    return result


def trivial_pwds(attributes, years, numbers, output_file):
    with open(output_file, "w+") as f:
        for elem in attributes:
            if len(elem) >= min_pwd_length:
                f.write(elem + "\n")
            if numbers:
                # Combine username with numbers
                for number in range_21:
                    pwd = elem + str(number)
                    if len(pwd) >= min_pwd_length:
                        f.write(pwd + "\n")
            for symbol in symbols:
                if len(elem) >= min_pwd_length:
                    if elem.lower() != elem.capitalize():
                        f.write(elem.lower() + symbol + "\n")
                        f.write(elem.upper() + symbol + "\n")
                        f.write(elem.capitalize() + symbol + "\n")
                    else:
                        f.write(elem + symbol + "\n")
                if numbers and len(elem)+len(str(numbers)) >= min_pwd_length:
                    for number in range(1, 2100):
                        if elem.lower() != elem.capitalize():
                            f.write(elem.lower() + symbol + str(number) + "\n")
                            f.write(elem.upper() + symbol + str(number) + "\n")
                            f.write(elem.capitalize() +
                                    symbol + str(number) + "\n")
                            f.write(elem.upper() + str(number) + "\n")
                            f.write(elem.lower() + str(number) + "\n")
                            f.write(elem.upper() + str(number) + symbol + "\n")
                            f.write(elem.lower() + str(number) + symbol + "\n")
                            f.write(elem.capitalize() + str(number) + "\n")
                            f.write(elem + str(number) + symbol + "\n")
                        else:
                            f.write(elem + symbol + str(number) + "\n")
                            f.write(elem + str(number) + "\n")
                            f.write(elem + str(number) + symbol + "\n")
                if years and len(elem) + 4 >= min_pwd_length:
                    for year in range(1985, 2000):
                        if elem.lower() != elem.capitalize():
                            f.write(elem.lower() + symbol + str(year) + "\n")
                            f.write(elem.upper() + symbol + str(year) + "\n")
                            f.write(elem.capitalize() +
                                    symbol + str(year) + "\n")
                        else:
                            f.write(elem + symbol + str(year) + "\n")
        # f.close()
        # cleanup_wordlist(output_file, output_file.split('.')[0]+'_cleaned.txt')


def permutations_first_round(attributes, years, numbers, output_file):
    valid_attributes = [attr for attr in attributes if attr != ""]
    subsets = create_permutations_with_repetition(valid_attributes, 2)
    with open(output_file, "a+") as f:
        for subset in subsets:
            par1, par2 = subset
            if len(par1) + len(par2) >= min_pwd_length:
                if par1.lower() != par1.capitalize():
                    f.write(par1.lower() + par2 + "\n")
                    f.write(par1.upper() + par2 + "\n")
                    f.write(par1.capitalize() + par2 + "\n")
                else:
                    f.write(par1 + par2 + "\n")
            if numbers and len(par1) + len(par2) + len(str(numbers)) >= min_pwd_length:
                if par1.lower() != par1.capitalize():
                    for number in range_21:
                        f.write(par1.lower() + par2 + str(number) + "\n")
                        f.write(par1.upper() + par2 + str(number) + "\n")
                        f.write(par1.capitalize() + par2 + str(number) + "\n")
                else:
                    for number in range_21:
                        f.write(par1 + par2 + str(number) + "\n")
            if years and len(par1) + len(par2) + 4 >= min_pwd_length:
                if par1.lower() != par1.capitalize():
                    for year in range(1985, 2000):
                        f.write(par1.lower() + par2 + str(year) + "\n")
                        f.write(par1.upper() + par2 + str(year) + "\n")
                        f.write(par1.capitalize() + par2 + str(year) + "\n")
                else:
                    for year in range(1985, 2000):
                        f.write(par1 + par2 + str(year) + "\n")
    return subsets


def permutations_second_round(subsets, years, numbers, output_file):
    with open(output_file, "a+") as f:
        for subset in subsets:
            par1, par2 = subset
            for symbol in symbols:
                if len(par1) + len(par2) + 1 >= min_pwd_length:
                    if par1.lower() != par1.capitalize():
                        f.write(par1.lower() + symbol + par2 + "\n")
                        f.write(par1.upper() + symbol + par2 + "\n")
                        f.write(par1.capitalize() + symbol + par2 + "\n")
                    else:
                        f.write(par1 + symbol + par2 + "\n")
                if numbers and len(par1) + len(par2) + 3 >= min_pwd_length:
                    if par1.lower() != par1.capitalize():
                        for number in range_21:
                            f.write(par1.lower() + symbol +
                                    par2 + str(number) + "\n")
                            f.write(par1.lower() + par2 +
                                    symbol + str(number) + "\n")
                            f.write(par1.upper() + symbol +
                                    par2 + str(number) + "\n")
                            f.write(par1.upper() + par2 +
                                    symbol + str(number) + "\n")
                            f.write(par1.capitalize() + symbol +
                                    par2 + str(number) + "\n")
                            f.write(par1.capitalize() + par2 +
                                    symbol + str(number) + "\n")
                    else:
                        for number in range_21:
                            f.write(par1 + symbol + par2 + str(number) + "\n")
                            f.write(par1 + par2 + symbol + str(number) + "\n")
                if years and len(par1) + len(par2) + 5 >= min_pwd_length:
                    if par1.lower() != par1.capitalize():
                        for year in range(1985, 2000):
                            f.write(par1.lower() + symbol +
                                    par2 + str(year) + "\n")
                            f.write(par1.lower() + par2 +
                                    symbol + str(year) + "\n")
                            f.write(par1.upper() + symbol +
                                    par2 + str(year) + "\n")
                            f.write(par1.upper() + par2 +
                                    symbol + str(year) + "\n")
                            f.write(par1.capitalize() + symbol +
                                    par2 + str(year) + "\n")
                            f.write(par1.capitalize() + par2 +
                                    symbol + str(year) + "\n")
                    else:
                        for year in range(1985, 2000):
                            f.write(par1 + symbol + par2 + str(year) + "\n")
                            f.write(par1 + par2 + symbol + str(year) + "\n")
    

def common_passwords(attributes, years, numbers, output_file):
    with open(output_file, "a+") as f:
        for elem in common_pwds:
            if len(elem) >= min_pwd_length:
                f.write(elem + "\n")

            if numbers:
                # Combine common passwords with numbers
                password_numbers = [elem + str(number)
                                    for number in range_21]
                for pwd in password_numbers:
                    f.write(pwd + "\n")
                    f.write(pwd + str(years) +"\n")
                    for attribute in attributes:
                        f.write(attribute + pwd+"\n")
                        f.write(pwd + attribute + "\n")


def generate_concatenated_passwords(words, numbers, special_chars, min_length):
    passwords = []
    for word1 in words:
        for word2 in words:
            if word1 != word2:
                password = word1 + word2
                if numbers:
                    password += str(random.randint(0, 9999))
                if special_chars:
                    password += random.choice(string.punctuation)
                if len(password) >= min_length:
                    passwords.append(password)
    return passwords


def generate_keyboard_pattern_passwords(numbers, special_chars, min_length):
    keyboard_patterns = [
        "1234567890",
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm",
        "123qwe",
        "admin",
        "letmein",
        "qwerty",
        "987654321",
        "asdfgh",
        "1234"
    ]
    passwords = []
    for pattern in keyboard_patterns:
        if numbers:
            password = pattern + str(random.randint(0, 9999))
        else:
            password = pattern
        if special_chars:
            password += random.choice(string.punctuation)
        if len(password) >= min_length:
            passwords.append(password)
    return passwords


def generate_phrase_passwords(phrases, numbers, special_chars, min_length):
    passwords = []
    for phrase in phrases:
        if numbers:
            password = phrase + str(random.randint(0, 9999))
        else:
            password = phrase
        if special_chars:
            password += random.choice(string.punctuation)
        if len(password) >= min_length:
            passwords.append(password)
    return passwords


def generate_random_passwords(length, numbers, special_chars, min_length):
    passwords = []
    charset = string.ascii_letters + string.digits
    for _ in range(10000):  # Generate 10,000 random passwords
        password = ''.join(random.choice(charset) for _ in range(length))
        if numbers:
            password += str(random.randint(0, 9999))
        if special_chars:
            password += random.choice(string.punctuation)
        if len(password) >= min_length:
            passwords.append(password)
    return passwords


def leet_pwds(leetall, output_file):
    pwds = []
    with open(output_file, "r+") as f:
        pwds = f.read().split()

    with open(output_file, "a+") as f:
        for elem in pwds:
            continues = False
            for key in leet_chars.keys():
                if key in elem:
                    continues = True
                    break

            if continues:
                if leetall:
                    possibles = []

                    for lower in elem.lower():
                        ll = leet_chars.get(lower, lower)
                        possibles.append((lower,) if ll ==
                                         lower else (lower, ll))

                    leets = ["".join(t) for t in itertools.product(*possibles)]

                    for leet in leets:
                        f.write(leet + "\n")
                else:
                    leet = (elem + ".")[:-1]

                    for char in leet_chars.keys():
                        leet = leet.replace(char, leet_chars[char])

                    f.write(leet + "\n")


class Person:
    def __init__(
        self,
        name=None,
        middle_name=None,
        surname=None,
        nickname=None,
        username=None,
        age=None,
        birth_day=None,
        birth_month=None,
        birth_year=None,
        email=None,
        birth_place=None,
        first_pet=None,
        favourite_band=None,
        person_keywords=None,
        initial_1=None,
        initial_2=None,
        initial_3=None,


    ):

        self.name = name
        self.middle_name = middle_name
        self.surname = surname
        self.nickname = nickname
        self.username = username
        self.age = age
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.email = email
        self.birth_place = birth_place
        self.first_pet = first_pet
        self.favourite_band = favourite_band
        self.person_keywords = person_keywords
        self.initial_1 = initial_1
        self.initial_2 = initial_2
        self.initial_3 = initial_3


def person(add_leet, years, leetall, numbers):
    print("Targeting a person.\n")
    
    # Get target details
    target = input_person()
    global output_file
    output_file = None
    
    # Determine the output file name based on available target info
    if target.name and target.surname:
        file_name = f"{target.name}-{target.surname}.txt"
    elif target.name:
        file_name = f"{target.name}.txt"
    else:
        file_name = "P-Gen-output.txt"

    # Set the full output path
    output_file = f"output/{file_name}"
    
    # Inform the user about the output file location
    print(f"Creating output file: {output_file}")
    
    # Get attributes related to the person
    attributes = attr_keywords_in_unique_list(target)
    attributes.extend(list((target.username, target.nickname, target.name, target.middle_name,
                            target.surname, target.initial_1, target.initial_2, target.initial_3)))
    # Remove any duplicates in the attributes list
    attributes = list(set(attributes))
    
    # Generate password sets based on various criteria
    trivial_pwds(attributes, years, numbers, output_file)
    common_passwords(attributes, years, numbers, output_file)
    
    # First-round permutations
    subsets = permutations_first_round(attributes, years, numbers, output_file)
    
    # Further permutation rounds
    permutations_second_round(subsets, years, numbers, output_file)
    permutations_third_round(subsets, years, numbers, output_file)
    
    # Apply leetspeak if specified
    if add_leet or leetall:
        leet_pwds(leetall, output_file)
    
    # Completion message
    print(f"Password generation completed. Output saved to {output_file}")




def input_person():
    target = Person()
    print(
        "Enter all the information you know. Leave blank and hit enter if you don't know.\n"
    )
    target.name = input("[>] Name: ") or ''
    target.initial_1 = target.name[0] if target.name else ''
    target.middle_name = input("[>] Middle Name: ") or ''
    target.initial_2 = target.middle_name[0] if target.middle_name else ''
    target.surname = input("[>] Surname: ") or ''
    target.initial_3 = target.surname[0] if target.surname else ''
    target.nickname = input("[>] Nickname: ") or ''
    target.username = input("[>] Username: ") or ''
    target.age = input("[>] Age: ") or ''
    target.birth_day = input("[>] Birth day: ") or ''
    target.birth_month = input("[>] Birth month: ") or ''
    target.birth_year = input("[>] Birth year(YYYY): ") or ''
    target.email = input("[>] Email: ").split("@")[0] if input("[>] Email: ") else ''
    target.birth_place = input("[>] Birth place: ") or ''
    target.first_pet = input("[>] First pet: ") or ''
    target.favourite_band = input("[>] Favourite Band / Team: ") or ''

    person_keywords = input(
        "[>] Useful keywords such as relative , favorite things (separated by comma): ")

    target.person_keywords = prepare_keywords(person_keywords)

    return target


class Company:
    def __init__(
        self,
        name=None,
        web_domain=None,
        birth_year=None,
        company_keywords=None,
    ):

        self.name = name
        self.web_domain = web_domain
        self.birth_year = birth_year
        self.company_keywords = company_keywords


def permutations_third_round(subsets, years, numbers, output_file):
    with open(output_file, "a+") as f:
        for subset in subsets:
            par1, par2 = subset
            for symbol in symbols:
                if len(par1) + len(par2) + 1 >= min_pwd_length:
                    if par1.lower() != par1.capitalize():
                        f.write(par1 + symbol + par2 + "\n")
                    else:
                        f.write(par1 + symbol + par2 + "\n")
                if numbers and len(par1) + len(par2) + 2 >= min_pwd_length:
                    for number in range_21:
                        f.write(par1 + symbol + par2 + str(number) + "\n")
                if years and len(par1) + len(par2) + 5 >= min_pwd_length:
                    for year in range(1985, 2000):
                        f.write(par1 + symbol + par2 + str(year) + "\n")


if __name__ == "__main__":
    global output_file
    parser = argparse.ArgumentParser(
        description="LongTongue - Password List Generator")
    parser.add_argument(
        "-l", "--leet", help="Generate LeetSpeak passwords", action="store_true"
    )
    parser.add_argument(
        "-la", "--leetall", help="Generate all possible LeetSpeak passwords", action="store_true"
    )
    parser.add_argument(
        "-n", "--numbers", help="Add numbers to the generated passwords", action="store_true"
    )
    parser.add_argument(
        "-y", "--years", help="Add years to the generated passwords", action="store_true"
    )
    parser.add_argument(
        "-c", "--concatenate",
        help="Generate passwords by concatenating common words",
        action="store_true",
    )
    parser.add_argument(
        "-k", "--keyboard",
        help="Generate passwords based on common keyboard patterns",
        action="store_true",
    )
    parser.add_argument(
        "-p", "--phrases",
        help="Generate passwords using common phrases",
        action="store_true",
    )
    parser.add_argument(
        "-r", "--random",
        help="Generate random passwords",
        action="store_true",
    )
    args = parser.parse_args()

    add_leet = args.leet
    leetall = args.leetall
    numbers = args.numbers
    years = args.years

    print(
        "LongTongue - Password List Generator\n"
        "This tool generates a list of possible passwords based on the provided information about the target.\n"
    )
    print("Choose your target:")

    person(add_leet, years, leetall, numbers)
    additional_passwords = []
    if args.concatenate:
        concatenated_passwords = generate_concatenated_passwords(
            common_pwds, numbers, True, min_pwd_length
        )       
        additional_passwords.extend(concatenated_passwords)
    if args.keyboard:
        keyboard_pattern_passwords = generate_keyboard_pattern_passwords(
            numbers, True, min_pwd_length
        )
        additional_passwords.extend(keyboard_pattern_passwords)
    if args.phrases:
        # Add common phrases or sentences here
        common_phrases = ["letmein", "password123"]
        phrase_passwords = generate_phrase_passwords(
            common_phrases, numbers, True, min_pwd_length
        )
        additional_passwords.extend(phrase_passwords)
    if args.random:
        random_passwords = generate_random_passwords(
            12, numbers, True, min_pwd_length
        )
        additional_passwords.extend(random_passwords)

        
    passwords = common_pwds + additional_passwords
    with open(output_file, "a+") as f:
        for password in passwords: 
            f.write(password)
