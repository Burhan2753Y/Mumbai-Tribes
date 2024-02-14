import random
import datetime

data = []
for i in range(250):
    name = f"{random.choice(['John', 'Jane', 'Michael', 'Emma', 'William', 'Olivia', 'Oliver', 'Sophia', 'Isabella', 'Ava', 'Emily', 'Ethan', 'Mia', 'Harper', 'Elijah', 'Amelia', 'James', 'Charlotte', 'Benjamin', 'Avery'])} {random.choice(['Smith', 'Johnson', 'Brown', 'Jones', 'Williams', 'Miller', 'Davis', 'Thomas', 'Garcia', 'Rodriguez', 'Wilson', 'Martinez', 'Anderson', 'Taylor', 'Hernandez', 'Moore', 'Martin', 'Jackson', 'Thompson', 'White', 'Lopez'])}"
    birthDate = f"{random.choice(range(1950, 2003))}-{random.choice(range(1,13))}-{random.choice(range(1,28))}"
    image = f"https://example.com/image{i}.jpg"
    data.append({
        "name": name,
        "birthDate": birthDate,
        "image": image
    })

print(json.dumps(data, indent=4))