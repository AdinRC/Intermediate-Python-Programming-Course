#  lambda arguments: expression

# add10 = lambda x: x + 10
# print(add10(5))
# 
# def add10_func(x):
#     return x + 10
# 
# mult = lambda x, y: x+y 
# print(mult(2,7))


# points2d = [(1,2), (15,1), (5,-1), (10,4)]
# 
# points2d_sorted = sorted(points2d)
# print(points2d)
# print(points2d_sorted)
# 
# def sort_by_y(x):
#     return x[1]
# 
# points2d_sorted = sorted(points2d, key=lambda x: x[1])
# print(points2d)
# print(points2d_sorted)
# 
# points2d_sorted = sorted(points2d, key=lambda x: x[0] + x[1])
# print(points2d)
# print(points2d_sorted)


# # map(func, seq)
# a = [1,2,3,4,5]
# b = map(lambda x: x+2, a)
# print(list(b)) 
# c = [x+2 for x in a]
# print(c)


# a = [1,2,3,4,5]
# b = filter(lambda x: x%2==0, a)
# print(list(b)) 
# c = [ x for x in a if x%2==0]
# print(c)


#  reduce(func, seq)
from functools import reduce
a = [1,2,3,4]

product_a = reduce(lambda x,y: x*y, a)
print (product_a)