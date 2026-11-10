import csv
from validator import validate_contact

seen_phones = set()
seen_emails = set()
clean = []

with open("contacts.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row["name"]
        phone = row["phone"]
        email = row["email"]
        valid, reason = validate_contact(name, phone, email)
        if not valid:
            print(f"Rejected: {name} - {reason}")
            continue
        if phone in seen_phones or email in seen_emails:
            print(f"Rejected: {name} - Duplicate")
            continue
        seen_phones.add(phone)
        seen_emails.add(email)
        clean.append(row)

with open("student_clean.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name","phone","email"])
    writer.writeheader()
    writer.writerows(clean)

print(f"Total Valid: {len(clean)}")
