def doll(n):
    if n >= 1000:
        return n-3
    else:
        return doll(doll(n + 5))


print(str(doll(999)))

