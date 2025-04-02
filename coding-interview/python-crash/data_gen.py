import json
import csv
import random
from decimal import Decimal

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from faker import Faker
from datetime import datetime

fake = Faker()


def generate_merchant_data(num_merchants=10):
    """
    Generate a list of merchant records. Each record is a dict with:
    - merchant_id (UUID)
    - merchant_name (Fake company)
    - merchant_type (category like 'Online', 'Retail', etc.)
    - country (Fake country)
    - rating (1.0 to 5.0)
    - metadata (dict with contact info)
    """
    merchant_type_list = ["Online", "Retail", "Service", "Wholesale", "Franchise"]
    merchants = []
    for _ in range(num_merchants):
        merchant_id = str(fake.uuid4())
        merchant_name = fake.company()
        merchant_type = random.choice(merchant_type_list)
        country = fake.country()
        rating = round(random.uniform(1, 5), 1)
        metadata = {
            "contact_email": fake.company_email(),
            "contact_phone": fake.phone_number(),
            "address": fake.address()
        }
        record = {
            "merchant_id": merchant_id,
            "merchant_name": merchant_name,
            "merchant_type": merchant_type,
            "country": country,
            "rating": rating,
            "metadata": metadata
        }
        merchants.append(record)
    return merchants


def generate_transaction_data(
        merchants,
        num_transactions=50,
        possible_currencies=None,
        transaction_types=None,
        categories_map=None
):
    """
    Generate transaction records referencing valid merchant_ids from the 'merchants' list.

    Each record includes:
    - user_id (UUID)
    - transaction_day (YYYY-MM-DD)
    - transaction_id (UUID)
    - merchant_id (from the merchants list)
    - amount (float)
    - currency (3-letter code)
    - transaction_type (purchase, refund, etc.)
    - risk_score (0-100)
    - merchant_category (derived or random, e.g., 'Clothing', 'Electronics', etc.)
    - timestamp (ISO 8601)
    - payment_method_type (credit_card, paypal, etc.)
    - metadata (additional JSON)

    'categories_map' can correlate merchant_type -> a set of possible categories.
    """
    if possible_currencies is None:
        possible_currencies = ["USD", "EUR", "GBP", "CAD", "AUD"]
    if transaction_types is None:
        transaction_types = ["purchase", "refund", "withdrawal", "deposit"]
    if categories_map is None:
        # Map of merchant_type -> possible categories
        categories_map = {
            "Online": ["E-commerce", "Electronics", "Clothing", "Entertainment"],
            "Retail": ["Grocery", "Clothing", "Automotive", "Health", "Travel"],
            "Service": ["Entertainment", "Health", "Travel", "Finance", "Education"],
            "Wholesale": ["Electronics", "Grocery", "Health", "Restaurant"],
            "Franchise": ["Automotive", "Clothing", "Restaurant", "Travel"]
        }

    transactions = []
    merchant_ids = [m["merchant_id"] for m in merchants]
    merchant_types_map = {m["merchant_id"]: m["merchant_type"] for m in merchants}

    for _ in range(num_transactions):
        user_id = str(fake.uuid4())
        transaction_day = fake.date(pattern="%Y-%m-%d")
        transaction_id = str(fake.uuid4())

        # Pick a random merchant from the merchants list
        chosen_merchant_id = random.choice(merchant_ids)
        chosen_merchant_type = merchant_types_map[chosen_merchant_id]

        amount = round(random.uniform(1, 99999999.99), 2)
        currency = random.choice(possible_currencies)
        transaction_type = random.choice(transaction_types)
        risk_score = random.randint(0, 100)

        # Derive merchant_category from the chosen_merchant_type
        # If type is 'Retail', pick from categories_map['Retail']
        merchant_category = random.choice(categories_map[chosen_merchant_type])

        timestamp = fake.date_time_between("-1y", "now").isoformat()
        payment_method_choices = ["credit_card", "debit_card", "paypal", "bank_transfer"]
        payment_method_type = random.choice(payment_method_choices)

        metadata = {
            "device_id": str(fake.uuid4()),
            "ip_address": fake.ipv4(),
            "geo_location": {
                "lat": fake.latitude(),
                "lng": fake.longitude()
            }
        }

        record = {
            "user_id": user_id,
            "transaction_day": transaction_day,
            "transaction_id": transaction_id,
            "merchant_id": chosen_merchant_id,
            "amount": amount,
            "currency": currency,
            "transaction_type": transaction_type,
            "risk_score": risk_score,
            "merchant_category": merchant_category,
            "timestamp": timestamp,
            "payment_method_type": payment_method_type,
            "metadata": metadata
        }
        transactions.append(record)

    return transactions


def write_merchants_csv(merchants, csv_file):
    fieldnames = [
        "merchant_id",
        "merchant_name",
        "merchant_type",
        "country",
        "rating",
        "metadata"
    ]
    with open(csv_file, "w", newline='', encoding="utf-8") as cf:
        writer = csv.DictWriter(cf, fieldnames=fieldnames)
        writer.writeheader()
        for rec in merchants:
            # Convert metadata to JSON string
            row = rec.copy()
            row["metadata"] = json.dumps(rec["metadata"], ensure_ascii=False)
            writer.writerow(row)


def write_merchants_parquet(merchants, parquet_file):
    """
    Convert the merchants list of dicts to a Pandas DataFrame, then write to Parquet.
    For the 'metadata' field (dict), we store it as a JSON string column.
    """
    merchant_rows = []
    for m in merchants:
        temp = m.copy()
        temp["metadata"] = json.dumps(m["metadata"], ensure_ascii=False)
        merchant_rows.append(temp)
    df = pd.DataFrame(merchant_rows)
    df.to_parquet(parquet_file, index=False)


def write_transactions_csv(transactions, csv_file):
    fieldnames = [
        "user_id",
        "transaction_day",
        "transaction_id",
        "merchant_id",
        "amount",
        "currency",
        "transaction_type",
        "risk_score",
        "merchant_category",
        "timestamp",
        "payment_method_type",
        "metadata"
    ]
    with open(csv_file, "w", newline='', encoding="utf-8") as cf:
        writer = csv.DictWriter(cf, fieldnames=fieldnames)
        writer.writeheader()
        for rec in transactions:
            row = rec.copy()
            row["metadata"] = json.dumps(rec["metadata"],default=decimal_to_float, ensure_ascii=False)
            writer.writerow(row)

def decimal_to_float(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    return obj

def write_transactions_parquet(transactions, parquet_file):
    """
    Convert transactions to a DataFrame, storing metadata as JSON string.
    """
    tx_rows = []
    for t in transactions:
        temp = t.copy()
        temp["metadata"] = json.dumps(t["metadata"],default=decimal_to_float, ensure_ascii=False)
        tx_rows.append(temp)
    df = pd.DataFrame(tx_rows)
    df.to_parquet(parquet_file, index=False)


if __name__ == "__main__":
    # Generate correlated data
    merchants_data = generate_merchant_data(num_merchants=10)
    transactions_data = generate_transaction_data(merchants_data, num_transactions=50)

    # Write Merchants to CSV and Parquet
    write_merchants_csv(merchants_data, "merchants.csv")
    write_merchants_parquet(merchants_data, "merchants.parquet")

    # Write Transactions to CSV and Parquet
    write_transactions_csv(transactions_data, "transactions.csv")
    write_transactions_parquet(transactions_data, "transactions.parquet")

    print("Generated merchants & transactions data in CSV and Parquet with enforced relationships.")