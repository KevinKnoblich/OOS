from faker import Faker
import pandas as pd
import random

fake = Faker('de_DE')
products = [{'pid': i,
             'branch': 1,
             'pname': fake.first_name(),
             'pcat': random.randint(1,4),
             'supplier': random.choice([fake.company(), 'OOS']),
             'price per unit in EUR': round(random.uniform(0.009,0.2),3)
              } for i in range(1, 21)]

products_df = pd.DataFrame(products)
products_df.to_csv('data/products.csv', index=False)
