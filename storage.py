def read_file(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            return f.readlines(), None
    except FileNotFoundError:
        return None, f"Файл {filename} не найден"

def save_ok(filename, good):
    with open(filename, "w", encoding="utf-8") as f:
        for a in good:
            f.write(f"{a['fio']};{a['mail']};{a['phone']};{a['group']}\n")

def save_errors(filename, bad):
    with open(filename, "w", encoding="utf-8") as f:
        for i, line, err in bad:
            f.write(f"строка {i}: {err}\n{line}\n")

if __name__ == "__main__":
    print("Модуль storage готов к работе")