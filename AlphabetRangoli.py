def print_rangoli(size):
    rows = []
    letters = [chr(i+97) for i in range(size-1,-1,-1)]
    base = "-".join(letters)

    for i in range(size):
        row = base[:len(base) - i*2]
        row = ("-" * (len(base) - len(row))) + row
        rows.insert(0, row)

    rows.extend(reversed(rows[:-1]))

    for i in range(len(rows)):
        row = rows[i]
        rev_row = row[::-1]
        rows[i] = row + rev_row[1:]
    print(*rows, sep="\n")






if __name__ == '__main__':
    # n = int(input())
    n = 3
    print_rangoli(n)