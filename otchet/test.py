def point_in_number(arr):  # расставляет точки в больших числах
    if arr < 0:
        s = list(str(arr)[1:])
    else:
        s = list(str(arr))

    count = 0
    i = 0
    while i < len(s) - 1:
        count += 1
        i += 1
        if count == 3:
            s.insert(len(s) - i, '.')
            count = 0
            i += 1
    if arr < 0:
        return "-" + "".join(s)
    else:
        return "".join(s)

print(point_in_number(-1000567))