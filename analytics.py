def show_report(students, total):
    valid = len(students)
    print("--- REPORT ---")
    print(f"Total: {total}, Valid: {valid}, Accuracy: {valid/total*100:.1f}%")
    telecom = {}
    domains = {}
    for s in students:
        first = s["phone"][0]
        telecom[first] = telecom.get(first, 0) + 1
        dom = s["email"].split("@")[1]
        domains[dom] = domains.get(dom, 0) + 1
    print("Telecom:", telecom)
    print("Email Domains:", domains)