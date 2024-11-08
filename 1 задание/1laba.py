def check(b,c):
    a = int(input("Введите число: "))
    if (a > 0):
        x = []
        x.append(a)
        x.append(b)
        x.append(c)
        max_el = 0
        for i in range(0,3):
            if (x[i] > max_el):
                max_el = x[i]
        return max_el
    else:
        return -1
            

print(check(1,4))
