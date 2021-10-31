# region count occurrence of each element in a iterable(like string)
from collections import Counter

test_str = 'uycbgfuyxnugfzuywgfxgrfqxu'  # random string
count = dict(Counter(test_str))
print(count)
# endregion


# region looping over multiple iterables at once
s = 'vgfvrewgver'  # string object
l = [i for i in range(len(s))]  # list object
m = map(lambda x: f'ascii({ord(x)})', s)  # map object

for i, j, k in zip(s, l, m):  # loops terminates when end of any iterable is reached
    print(f'string:{i}--list:{j}--map:{k}')


# endregion


# region apply a function to all elements of an iterable
def function(x):
    return x * x


List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
map1 = map(function, List)  # returns map object
l1 = list(map1)  # converts the map to list
print(l1)

'''It can also be done without defining any function by using lambda function'''
map2 = map(lambda x: x * x, List)
l2 = list(map2)
print(l2)

# endregion


# region find gcd and lcm
from math import gcd

a, b = 123515, 584533383
g = gcd(a, b)
lcm = (a * b) // g

# endregion
