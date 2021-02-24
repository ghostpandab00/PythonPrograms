def fact(num):
    if num == 0:
        return 1
    return num * fact(num - 1)


count = int(input("Enter the count: "))
result = fact(count)
print(result)
