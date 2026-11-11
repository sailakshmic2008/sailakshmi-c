import csv
from validator import validate_contact
from analytics import generate_report

students = []
with open("student_clean.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        students.append(row)

def save():
    with open("student_clean.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["name","phone","email"])
        w.writeheader()
        w.writerows(students)

while True:
    print("\n1.View 2.Search 3.Add 4.Update 5.Delete 6.Report 7.Exit")
    ch = input("Enter choice: ")
    if ch == "1":
        for s in students: print(s)
    elif ch == "2":
        key = input("Enter phone/name: ")
        for s in students:
            if key in s["phone"] or key.lower() in s["name"].lower():
                print(s)
    elif ch == "3":
        n = input("Name: "); p = input("Phone: "); e = input("Email: ")
        v, r = validate_contact(n, p, e)
        if not v: print(r)
        else: students.append({"name":n,"phone":p,"email":e}); print("Added")
    elif ch == "4":
        p = input("Enter phone to update: ")
        for s in students:
            if s["phone"] == p:
                s["name"] = input("New Name: "); print("Updated")
    elif ch == "5":
        p = input("Enter phone to delete: ")
        students = [s for s in students if s["phone"] != p]
        print("Deleted")
    elif ch == "6":
        generate_report()
    elif ch == "7":
        save(); print("Saved. Bye!"); break
