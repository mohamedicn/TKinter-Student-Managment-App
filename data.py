from faker import Faker
import json

faker = Faker()
data = {}


sessions = ("2024-1", "2024-3", "2024-6", "2024-9", "2024-12", "2025-3", "2025-6", "2025-9", "2025-12")

for i in range(1, 1001):  
    data[i] = {
        "session": faker.random_element(elements=sessions),  
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "class": str(faker.random_int(min=1, max=3)),
        "section": faker.random_element(elements=("A", "B", "C")),
        "gender": faker.random_element(elements=("Male", "Female")),
        "mobile": faker.phone_number(),
        "address": faker.country()
    }

with open("fake_data.json", "w") as f:
    json.dump(data, f, indent=2)

print("Fake data saved to 'fake_data.json'")
