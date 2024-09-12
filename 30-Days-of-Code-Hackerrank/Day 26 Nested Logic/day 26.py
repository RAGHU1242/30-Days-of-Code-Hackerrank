def calculate_fine(returned, due):
    d1, m1, y1 = returned
    d2, m2, y2 = due

    if y1 > y2:
        return 10000
    elif y1 == y2:
        if m1 > m2:
            return 500 * (m1 - m2)
        elif m1 == m2 and d1 > d2:
            return 15 * (d1 - d2)

    return 0

returned_date = list(map(int, input().split()))
due_date = list(map(int, input().split()))

fine = calculate_fine(returned_date, due_date)
print(fine)
