from faker import Factory
from random import randint

fake = Factory.create('en_CA')

def generate_fake_name():
    fake_name = fake.name()
    return fake_name

def generate_fake_address():
    fake_address = fake.address().replace('\n', ', ')
    return fake_address

def generate_fake_date_of_birth():
    fake_dob = fake.date_of_birth(minimum_age=18, maximum_age=90)
    return fake_dob.strftime("%m/%d/%Y")

def get_first_letter_second_word(sentence):
   words = sentence.split()
   if len(words) >= 2:
       second_word = words[1]
       first_letter = second_word[0]
       return first_letter
   else:
       return None

def generate_drivers_license(name, dob):
    letter = get_first_letter_second_word(name)
    sequence_1 = fake.random_number(digits=4)
    sequence_2 = fake.random_number(digits=5)
    fake.random_int(min=1950, max=2023)
    month, day, year = dob.split('/')
    fake_drivers_license = f"{letter}{sequence_1}-{sequence_2}-{year[3]}{month}{day}"
    return fake_drivers_license

def generate_fake_sin():
    sin_digits = [str(randint(0, 9)) for _ in range(9)]
    sin_number = ''.join(sin_digits)
    fake_sin_number = f"{sin_number[:3]} {sin_number[3:6]} {sin_number[6:]}"
    return fake_sin_number

def generate_random_int():
    sequence_1 = fake.random_number(digits=randint(1,4))
    sequence_2 = fake.random_number(digits=randint(1,4))
    sequence_3 = fake.random_number(digits=randint(1,4))
    space_or_delimited = ' ' if randint(0,1) == 1 else '-'
    random_int_string = f"{sequence_1}{space_or_delimited}{sequence_2}{space_or_delimited}{sequence_3}"
    return random_int_string