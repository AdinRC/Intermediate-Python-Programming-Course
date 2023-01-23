#  Sets: unordered, mutable, no duplicates

# myset = {1,2,3,1,2}
# print(myset)


# myset = set([1,2,3])
# print(myset)


# myset = set("Hello")
# print(myset)


# myset = {}
# print(type(myset))


# myset = set()
# myset.add(1)
# myset.add(2)
# myset.add(3)
# 
# myset.remove(2)
#myset.discard(4)
# myset.clear()
# 
# print(myset.pop())
# print(myset)
# 
# for x in myset:
#     print(x)
# 
# if 2 in myset:
#     print("yes")


# odds = {1,3,5,7,9}
# evens = {0,2,4,6,8}
# primes = {2,3,5,7}
# 
# u = odds.union(evens)
# print(u)
# 
# i = odds.intersection(evens)
# print(i)
# 
# i = odds.intersection(primes)
# print(i)
# 
# i = evens.intersection(primes)
# print(i)


# setA = {1,2,3,4,5,6,7,8,9}
# setB = {1,2,3,10,11,12}
# 
# diff = setA.difference(setB)
# print(diff)
# 
# diff = setB.difference(setA)
# print(diff)
# 
# diff = setB.symmetric_difference(setA)
# print(diff)
# 
# setA.update(setB)
# print(setA)
# 
# setA.intersection_update(setB)
# print(setA)
# 
# setA.difference_update(setB)
# print(setA)
# 
# setA.symmetric_difference_update(setB)
# print(setA)


# setA = {1,2,3,4,5,6}
# setB = {1,2,3}
# 
# print(setA.issubset(setB))
# print(setB.issubset(setA))
# 
# print(setA.issuperset(setB))
# print(setB.issuperset(setA))


# setA = {1,2,3,4,5,6}
# setB = {1,2,3}
# setC = {7,8}
# 
# print(setA.isdisjoint(setB))
# print(setA.isdisjoint(setC))


# setA = {1,2,3,4,5,6}
# 
# setB = setA
# setB.add(7)
# print(setB)
# print(setA)
# 
# setB = setA.copy() or setB = set(setA)
# setB.add(7)
# print(setB)
# print(setA)


# frozenset cannot change the element it will show error
# a = frozenset([1, 2, 3, 4])
# 
# a.add(5)
# 
# print(a)