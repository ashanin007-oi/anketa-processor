def check_fio(raw):
    parts = raw.split()
    if len(parts) < 2:
        return None, "в ФИО меньше двух слов"
    fio = " ".join(p.capitalize() for p in parts)
    return fio, None

def check_mail(raw):
    mail = raw.strip().lower()
    if mail.count("@") != 1:
        return None, "почта неверная: " + raw
    left, right = mail.split("@")
    if not left or not right:
        return None, "почта неверная: " + raw
    if "." not in right:
        return None, "почта неверная: " + raw
    if right.startswith(".") or right.endswith("."):
        return None, "почта неверная: " + raw
    return mail, None

def check_phone(raw):
    digits = "".join(ch for ch in raw if ch.isdigit())
    if len(digits) != 11:
        return None, f"телефон: нужно 11 цифр, получено {len(digits)}"
    if digits[0] not in "78":
        return None, "телефон должен начинаться с 7 или 8"
    phone = f"+7 ({digits[1:4]}) {digits[4:7]}-{digits[7:9]}-{digits[9:11]}"
    return phone, None

def check_group(raw):
    group = raw.replace(" ", "").lower()
    if not group:
        return None, "пустая группа"
    return group, None

def parse_line(line):
    parts = line.strip().split(";")
    if len(parts) != 4:
        return None, f"полей не 4, а {len(parts)}"
    fio_raw, mail_raw, phone_raw, group_raw = parts
    
    fio, err = check_fio(fio_raw)
    if err: return None, err
    
    mail, err = check_mail(mail_raw)
    if err: return None, err
        
    phone, err = check_phone(phone_raw)
    if err: return None, err
        
    group, err = check_group(group_raw)
    if err: return None, err
    
    return {"fio": fio, "mail": mail, "phone": phone, "group": group}, None

if __name__ == "__main__":
    print("Модуль validators готов к работе")