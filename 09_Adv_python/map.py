# numbers = [1,4,5,67,7]

# def square (x):
#     return x*x

# new =  list(map(square, numbers))
# print (new)

# def is_greater_than9(x):
#     if x >= 9:
#         return True

#     else:
#         return False

# a = [1,3,4,554,332,56,789,98776,44,33,12,1,4,6,7,9,0] 

# new = list(filter (is_greater_than9, a))
# print(new)

from functools import reduce

a = [1,2,3,4]

def sum(a,b):
    return a-b

c = reduce(sum,a)
print( c )