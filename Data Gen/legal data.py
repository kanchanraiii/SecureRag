import json
import random
from faker import Faker

fake = Faker("en_IN")
NUM_RECORDS = 10000

def random_noise(text):
    if random.random() < 0.15:
        idx = random.randint(0, len(text)-1)
        return text[:idx] + random.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ") + text[idx+1:]
    return text

def generate_legal_record():
    client_name = fake.company()
    agreement_date = fake.date_this_decade().isoformat()
    contract_type = random.choice(["NDA", "Service Agreement", "Lease Contract", "Employment Contract"])
    court_case_number = fake.bothify(text="C-####-2025")
    court_status = random.choice(["Pending", "Closed", "Appeal Filed", "Dismissed"])
    return {
        "client_company": random_noise(client_name),
        "agreement_type": random_noise(contract_type),
        "agreement_date": random_noise(agreement_date),
        "court_case": {
            "case_number": random_noise(court_case_number),
            "status": random_noise(court_status)
        },
        "nda_details": "Confidentiality agreement between parties.",
        "email": random_noise(fake.company_email()),
        "phone": random_noise(fake.phone_number()),
        "address": random_noise(fake.address().replace("\n", ", ")),
    }

def write_records(filename, generator):
    with open(filename, "w", encoding="utf-8") as f:
        for _ in range(NUM_RECORDS):
            record = generator()
            f.write(json.dumps(record) + "\n")
    print(f"✅ Generated {NUM_RECORDS} legal records → {filename}")

if __name__ == "__main__":
    write_records("legal_dataset.jsonl", generate_legal_record)
