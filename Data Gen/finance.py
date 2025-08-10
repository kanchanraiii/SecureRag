import json
import random
from faker import Faker

fake = Faker("en_IN")  # Indian PII style
NUM_RECORDS = 10000

def random_noise(text):
    if random.random() < 0.15:
        idx = random.randint(0, len(text)-1)
        return text[:idx] + random.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ") + text[idx+1:]
    return text

def generate_finance_record():
    account_number = fake.bban()
    balance = round(random.uniform(1000, 1000000), 2)
    transaction_amount = round(random.uniform(10, 50000), 2)
    loan_amount = round(random.uniform(50000, 1000000), 2)
    loan_status = random.choice(["approved", "pending", "rejected"])
    return {
        "name": random_noise(fake.name()),
        "account_number": random_noise(account_number),
        "balance": balance,
        "loan_application": {
            "amount": loan_amount,
            "status": loan_status,
            "application_date": random_noise(fake.date_this_decade().isoformat())
        },
        "transaction_history": [
            {
                "date": random_noise(fake.date_this_year().isoformat()),
                "amount": transaction_amount,
                "type": random.choice(["debit", "credit"]),
                "description": random_noise(fake.bs())
            }
            for _ in range(random.randint(1,5))
        ],
        "email": random_noise(fake.email()),
        "phone": random_noise(fake.phone_number()),
        "pan": random_noise(fake.bothify(text="?????#####", letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ")),
    }

def write_records(filename, generator):
    with open(filename, "w", encoding="utf-8") as f:
        for _ in range(NUM_RECORDS):
            record = generator()
            f.write(json.dumps(record) + "\n")
    print(f"✅ Generated {NUM_RECORDS} finance records → {filename}")

if __name__ == "__main__":
    write_records("../Data/finance_dataset.jsonl", generate_finance_record)
