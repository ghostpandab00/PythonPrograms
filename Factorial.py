def fact(num):
    f = 1
    for i in range(1, count + 1):
        f = f * i
    return f


count = int(input("Enter the count: "))
result = fact(count)
print(result)
