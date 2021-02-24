from functools import reduce

nums = [1, 3, 54, 78, 9, 99]

evens = list(filter(lambda n: n % 2 == 0, nums))

doubles = list(map(lambda n: n * 2, evens))

sums = reduce(lambda a, b: a + b, doubles)

print(sums)
