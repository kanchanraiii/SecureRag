import json
import random
from faker import Faker

fake = Faker("en_IN")  
NUM_RECORDS = 2000
OUTPUT_FILE = "ecommerce_dataset.jsonl"

def random_noise(text):
    """Add typos / OCR-like noise to increase data variety."""
    if random.random() < 0.15:
        idx = random.randint(0, len(text) - 1)
        return text[:idx] + random.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ") + text[idx+1:]
    return text

product_categories = [
    "Electronics", "Clothing", "Home & Kitchen", "Sports", "Books", 
    "Beauty & Personal Care", "Toys", "Automotive", "Grocery", "Furniture"
]

payment_methods = ["Credit Card", "Debit Card", "UPI", "Net Banking", "Cash on Delivery", "Wallet"]

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for _ in range(NUM_RECORDS):
        order_id = f"ORD{random.randint(100000, 999999)}"
        record = {
            "order_id": random_noise(order_id),
            "customer_name": random_noise(fake.name()),
            "email": random_noise(fake.email()),
            "phone": random_noise(fake.phone_number()),
            "shipping_address": random_noise(fake.address().replace("\n", ", ")),
            "billing_address": random_noise(fake.address().replace("\n", ", ")),
            "product_name": random_noise(fake.word().capitalize() + " " + random.choice(product_categories)),
            "category": random.choice(product_categories),
            "quantity": random.randint(1, 5),
            "unit_price": round(random.uniform(200, 20000), 2),
            "payment_method": random.choice(payment_methods),
            "card_number": random_noise(str(fake.credit_card_number(card_type=None))),
            "card_expiry": fake.credit_card_expire(),
            "cvv": str(random.randint(100, 999)),
            "order_date": fake.date_this_decade().isoformat(),
            "delivery_date": fake.date_this_year().isoformat(),
            "notes": random_noise(fake.text(max_nb_chars=100))
        }
        f.write(json.dumps(record) + "\n")

print(f"✅ Generated {NUM_RECORDS} synthetic E-Commerce & Retail records → {OUTPUT_FILE}")
