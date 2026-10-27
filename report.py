def mask_phone(phone):
    digits = "".join(ch for ch in phone if ch.isdigit())
    return f"+7 ({digits[1:4]}) ***-**-{digits[-2:]}"

def print_table(good):
    print(f"{'№':>3} {'ФИО':<30} {'Почта':<25} {'Телефон':<20} {'Группа':<8}")
    for idx, a in enumerate(good, 1):
        fio = a["fio"][:30]
        mail = a["mail"][:25]
        phone = mask_phone(a["phone"])
        group = a["group"]
        print(f"{idx:>3} {fio:<30} {mail:<25} {phone:<20} {group:<8}")

def print_errors(bad):
    print(f"Отклонено строк: {len(bad)}")
    for i, line, err in bad:
        print(f"строка {i}: {err}")
        print(line)

def print_stats(total, good, bad, lines):
    print(f"Всего строк в файле: {len(lines)}")
    print(f"Принято: {len(good)} | Отклонено: {len(bad)}")
    stat = {}
    for a in good:
        stat[a["group"]] = stat.get(a["group"], 0) + 1
    print("По группам:")
    for g in sorted(stat):
        print(f"{g} {stat[g]}")

if __name__ == "__main__":
    print("Модуль report готов к работе")