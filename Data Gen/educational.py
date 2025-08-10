import json
import random
from faker import Faker

fake = Faker("en_IN")  # Indian education context for realism
NUM_RECORDS = 2000
OUTPUT_FILE = "education_dataset.jsonl"

def random_noise(text):
    """Add small typos or OCR-like noise for variety."""
    if random.random() < 0.15:
        idx = random.randint(0, len(text) - 1)
        return text[:idx] + random.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ") + text[idx+1:]
    return text

degrees = [
    "B.Tech", "B.Sc", "B.A", "M.Tech", "M.Sc", "M.A", 
    "PhD", "Diploma", "MBA", "LLB"
]

majors = [
    "Computer Science", "Physics", "Mathematics", "Economics", "History",
    "Mechanical Engineering", "Electrical Engineering", "Biotechnology", 
    "Political Science", "Business Administration"
]

grades = ["A+", "A", "B+", "B", "C", "D", "F"]

enrollment_statuses = ["Active", "Graduated", "Suspended", "On Leave", "Withdrawn"]

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for _ in range(NUM_RECORDS):
        student_id = f"STU{random.randint(100000, 999999)}"
        record = {
            "student_id": random_noise(student_id),
            "full_name": random_noise(fake.name()),
            "email": random_noise(fake.email()),
            "phone": random_noise(fake.phone_number()),
            "address": random_noise(fake.address().replace("\n", ", ")),
            "date_of_birth": fake.date_of_birth(minimum_age=17, maximum_age=35).isoformat(),
            "degree_program": random.choice(degrees),
            "major": random.choice(majors),
            "enrollment_year": random.randint(2010, 2025),
            "graduation_year": random.choice([None, random.randint(2014, 2030)]),
            "enrollment_status": random.choice(enrollment_statuses),
            "gpa": round(random.uniform(2.0, 4.0), 2),
            "current_semester": random.randint(1, 8),
            "grades": {fake.word(): random.choice(grades) for _ in range(random.randint(3, 6))},
            "student_notes": random_noise(fake.text(max_nb_chars=120))
        }
        f.write(json.dumps(record) + "\n")

print(f"✅ Generated {NUM_RECORDS} synthetic Education & Academia records → {OUTPUT_FILE}")

