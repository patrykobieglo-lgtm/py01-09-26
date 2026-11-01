def suma_do(n):
    if n == 0:
        return 0
    return n + suma_do(n-1)

print(suma_do(6))
