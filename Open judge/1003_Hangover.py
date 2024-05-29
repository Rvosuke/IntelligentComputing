while True:
    s = float(input())
    if s <= 0 or s >= 5.20:
        break

    n = 0
    sums = 0
    while sums < s:
        n += 1
        sums += 1 / (n + 1)

    print(f"{n} card(s)")
