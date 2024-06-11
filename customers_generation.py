from faker import Faker
import pandas as pd
import random

fake = Faker('de_DE')
customers = [{'cid': i,
             'cfname': fake.first_name(),
             'clname': fake.last_name(),
             'ccompany': fake.company(),
             'phone_nr': fake.phone_number(),
              } for i in range(1, 1001)]

customers_df = pd.DataFrame(customers)
customers_df.to_csv('data/customers.csv', index=False)
