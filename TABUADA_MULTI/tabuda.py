while True:
    n = int(input("write a number: "))
    if n < 0:
        break
    for i in range(1, 11):
        s = n * i
        print(f"{n} * {i} = {s}")

