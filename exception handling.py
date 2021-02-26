a = 5
b = 0

try:
    print("Resource open")
    print(a / b)
    num = int(input("Enter a number :"))
    print(num)
except ZeroDivisionError as e:
    print("Hey, you can not divide a number by Zero" , e)
except ValueError as e:
    print("Invalid Input" , e)
except Exception as e:
    print("Something went wrong" , e)
finally:
    print("Resource closed")
