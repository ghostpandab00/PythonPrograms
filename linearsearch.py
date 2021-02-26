pos = 0


def search(list, searchitem):
    i = 0
    while i < len(lst):
        if lst[i] == searchItem:
            globals()['pos'] = i
            return True
        i = i + 1
    return False


lst = []  # creating an empty list
n = int(input("Enter the number of elements: "))  # number of elements as input
for i in range(0, n):  # iterating till the range
    ele = int(input())
    lst.append(ele)  # adding the element
print(lst)

searchItem = int(input("Enter the search element: "))

if search(lst, searchItem):
    print("Found at", pos+1)
else:
    print("Not found")
