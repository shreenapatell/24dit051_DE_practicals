import pandas as pd
import sqlite3
import json
import os
import logging

from faker import Faker
import random
fake = Faker()

customers = []

for i in range(50):

    customers.append({
        "CustomerID": i + 1,
        "Name": fake.name(),
        "Email": fake.email(),
        "Phone": fake.phone_number(),
        "Age": random.randint(18, 70)
    })

df = pd.DataFrame(customers)

df.to_csv("data/customers.csv", index=False)

print(df.head())
transactions = []

for i in range(20):

    transactions.append({

        "transaction_id": 1000 + i,

        "customer": {
            "id": random.randint(1, 50),
            "name": fake.name()
        },

        "payment": {
            "amount": random.randint(100, 5000),
            "method": random.choice(["UPI", "Card", "Cash"])
        }

    })

with open("data/api_transactions.json", "w") as f:
    json.dump(transactions, f, indent=4)

print("API transaction JSON created successfully!")
config = """

Server=localhost

Database=CustomerDB

Timeout=60

Version=1.0

"""

with open("data/config.txt", "w") as f:
    f.write(config)

print("Configuration file created successfully!")
print("\n----- CSV Schema -----")

df = pd.read_csv("data/customers.csv")

print(df.dtypes)

print("\n----- JSON Schema -----")

with open("data/api_transactions.json", "r") as f:
    data = json.load(f)

print(data[0].keys())
print("\n----- CSV Schema -----")

df = pd.read_csv("data/customers.csv")

print(df.dtypes)

print("\n----- JSON Schema -----")

with open("data/api_transactions.json", "r") as f:
    data = json.load(f)

print(data[0].keys())
print("\n----- Dataset Information -----")

print(df.info())

print("\n----- Dataset Statistics -----")

print(df.describe())

print("\n----- Missing Values -----")

print(df.isnull().sum())
df.loc[5, "Email"] = None

# Make Age column object type before inserting a string
df["Age"] = df["Age"].astype(object)
df.loc[10, "Age"] = "Unknown"

df.to_csv("data/customers.csv", index=False)

print("Bad data inserted successfully.")


bad = []
good = []

for index, row in df.iterrows():

    if pd.isnull(row["Email"]) or pd.isnull(row["Age"]):

        bad.append(row)

    else:

        good.append(row)

pd.DataFrame(bad).to_csv("data/quarantine.csv", index=False)

pd.DataFrame(good).to_csv("data/clean_customers.csv", index=False)

print("Quarantine file created successfully.")

conn = sqlite3.connect("customer.db")

clean = pd.read_csv("data/clean_customers.csv")

clean.to_sql("Customers", conn, if_exists="replace", index=False)

conn.close()

print("SQLite database created successfully.")

logging.basicConfig(
    filename="data/quality_log.txt",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logging.info("Customer data loaded.")
logging.warning("Missing email detected.")
logging.warning("Missing age detected.")

print("Log file created successfully.")

print("\nCSV Files Found")

for file in os.listdir("data"):

    if file.endswith(".csv"):

        dataframe = pd.read_csv("data/" + file)

        print(file)

        print(dataframe.shape)

        df = pd.read_csv("data/customers.csv")

bad = df[df["CustomerID"].isnull()]

good = df[df["CustomerID"].notnull()]

bad.to_csv("data/quarantine_primarykey.csv", index=False)

good.to_csv("data/validated.csv", index=False)

print("Primary key validation completed.")

if len(bad) > 0:

    logging.warning(str(len(bad)) + " records missing CustomerID.")

print("Alerts generated.")

print("\n========== FINAL REPORT ==========")

print("Total Records :", len(df))

print("Missing Emails :", df["Email"].isnull().sum())

print("Missing Age :", df["Age"].isnull().sum())

print("Valid Records :", len(good))

print("Invalid Records :", len(bad))