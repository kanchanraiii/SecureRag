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

def generate_healthcare_record():
    patient_id = fake.bothify(text="PID#####")
    prescription_date = fake.date_this_year().isoformat()
    diagnosis = random.choice([
        "Diabetes Mellitus", "Hypertension", "Common Cold", "Asthma",
        "Bronchitis", "Migraine", "Arthritis"
    ])
    medicines = [fake.word().capitalize() for _ in range(random.randint(1,3))]
    lab_test = random.choice(["Blood Test", "X-Ray", "MRI", "CT Scan", "Urine Test"])
    lab_result = random.choice(["Normal", "Abnormal", "Requires Follow-up"])
    return {
        "patient_name": random_noise(fake.name()),
        "patient_id": random_noise(patient_id),
        "dob": random_noise(fake.date_of_birth(minimum_age=0, maximum_age=90).isoformat()),
        "diagnosis": random_noise(diagnosis),
        "prescriptions": [
            {
                "medicine": med,
                "dosage": f"{random.randint(1,2)} tablets {random.randint(1,3)} times a day"
            } for med in medicines
        ],
        "lab_reports": [
            {
                "test": lab_test,
                "date": random_noise(prescription_date),
                "result": random_noise(lab_result)
            }
        ],
        "email": random_noise(fake.email()),
        "phone": random_noise(fake.phone_number()),
        "address": random_noise(fake.address().replace("\n", ", ")),
    }

def write_records(filename, generator):
    with open(filename, "w", encoding="utf-8") as f:
        for _ in range(NUM_RECORDS):
            record = generator()
            f.write(json.dumps(record) + "\n")
    print(f"✅ Generated {NUM_RECORDS} healthcare records → {filename}")

if __name__ == "__main__":
    write_records("healthcare_dataset.jsonl", generate_healthcare_record)
