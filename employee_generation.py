from faker import Faker
import pandas as pd
import random


def calculate_checksum(tid):
    """
    checksum digit for a given 10-digit German tax identification number
    """
    factors = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
    summ = 0
    for i, digit in enumerate(tid):
        product = int(digit) * factors[i]
        if product > 9:
            product = (product // 10) + (product % 10)
        summ += product
    checksum = (10 - (summ % 10)) % 10
    return checksum


def gen_tax_id():
    """
    Generates a valid random German tax identification number (Steuer-ID)
    """
    first_ten_digits = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    checksum = calculate_checksum(first_ten_digits)
    tax_id = first_ten_digits + str(checksum)
    return tax_id


fake = Faker('de_DE')

employees = [{'id': i,
              'branch': 1,
              'fname': fake.first_name(),
              'lname': fake.last_name(),
              'birthday': fake.date_of_birth(minimum_age=16, maximum_age=60),
              'address': fake.address(),
              'phone_nr': fake.phone_number(),
              'IBAN': fake.iban(),
              'TIN': gen_tax_id()} for i in range(1, 401)]

employees_df = pd.DataFrame(employees)
employees_df['email'] = employees_df['lname']+'@oos.de'
employees_df.to_csv('data/employees.csv', index=False)
