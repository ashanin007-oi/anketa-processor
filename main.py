from validators import parse_line
from storage import read_file, save_ok, save_errors
from report import print_table, print_errors, print_stats

FIO_FILE = "anketa.txt"
OK_FILE = "ok.txt"
ERR_FILE = "errors.txt"

def main():
    lines, err = read_file(FIO_FILE)
    if err:
        print(err)
        return

    good = []
    bad = []
    total = 0

    for i, line in enumerate(lines, 1):
        if line.strip() == "":
            continue
        total += 1
        anketa, err = parse_line(line)
        if err:
            bad.append((i, line.strip(), err))
        else:
            good.append(anketa)

    good.sort(key=lambda a: a["fio"])

    print_table(good)
    print_errors(bad)
    print_stats(total, good, bad, lines)
    
    save_ok(OK_FILE, good)
    save_errors(ERR_FILE, bad)
    print(f"Сохранено: {OK_FILE} и {ERR_FILE}")

if __name__ == "__main__":
    main()