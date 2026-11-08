def validate_contact(name, phone, email):
    if name.strip() == "":
        return False, "Missing Name"
    if len(phone) != 10 or not phone.isdigit() or phone[0] not in "6789":
        return False, "Invalid Phone"
    if email.count("@") != 1 or" "in email:
        return False, "Bad Email"
    domain = email.split("@") [1]
    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False, "Bad Email"
    return True, "Valid"
