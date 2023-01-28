# def mygenerators():
#     yield 1
#     yield 2
#     yield 3
# 
# g = mygenerators()
# print (g)
# for i in g:
#     print (i)
# 
# value = next(g)
# print (value)
# value = next(g)
# print (value)
#
# print(sum(g))
# print(sorted(g, reverse=True))


# def countdown(num):
#     print ("Starting")
#     while num > 0:
#         yield num
#         num -= 1
# 
# cd = countdown(4)
# value = next(cd)
# print (value)
# print (next(cd))

import sys
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

# print(firstn(10))
# mylist = firstn(10)
# print(mylist)
    
def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sys.getsizeof(firstn(1000000)))
print(sys.getsizeof(firstn_generator(1000000)))

