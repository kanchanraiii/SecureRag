import json
import random
from faker import Faker

fake = Faker("en_IN")  
NUM_RECORDS = 2000
OUTPUT_FILE = "govt_dataset.jsonl"

def random_noise(text):
    """Add random typos / OCR-like noise to increase data diversity."""
    if random.random() < 0.15:  
        idx = random.randint(0, len(text)-1)
        return text[:idx] + random.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ") + text[idx+1:]
    return text

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for _ in range(NUM_RECORDS):
        record = {
            "name": random_noise(fake.name()),
            "email": random_noise(fake.email()),
            "phone": random_noise(fake.phone_number()),
            "address": random_noise(fake.address().replace("\n", ", ")),
            "aadhaar": random_noise(str(random.randint(100000000000, 999999999999))),  # 12-digit Aadhaar
            "pan": random_noise(fake.bothify(text="?????#####", letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ")),
            "dob": random_noise(fake.date_of_birth(minimum_age=18, maximum_age=80).isoformat()),
            "notes": random_noise(fake.text(max_nb_chars=100))  # unstructured notes with possible PII
        }
        f.write(json.dumps(record) + "\n")

print(f"✅ Generated {NUM_RECORDS} synthetic PII records → {OUTPUT_FILE}")
