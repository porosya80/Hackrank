def print_rangoli(size):
    rows = []
    letters = "-".join([chr(i + 97) for i in range(size - 1, -1, -1)])

    for i in range(size):
        rows.insert(0, ("-" * (i * 2)) + letters[: len(letters) - i * 2])

    rows.extend(reversed(rows[:-1]))

    for i, row in enumerate(rows):
        rev_row = row[::-1]
        rows[i] = row + rev_row[1:]
    print(*rows, sep="\n")


if __name__ == "__main__":
    n = int(input())

    print_rangoli(n)
