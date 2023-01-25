# collections: Counter, named tuple, OrderedDict, defaultdict, deque


# from collections import Counter
# 
# a = "aaaaaabbbbbcccc"
# my_counter = Counter(a)
# print(my_counter)
# print(my_counter.items())
# print(my_counter.keys())
# print(my_counter.values())
# print(my_counter.most_common())
# print(my_counter.most_common(1))
# print(my_counter.most_common(2))
# print(my_counter.most_common(5))
# print(my_counter.most_common(1)[0])
# print(my_counter.most_common(1)[0][0])
# print(my_counter.elements())
# print(list(my_counter.elements()))


# from collections import namedtuple
# Point = namedtuple('Point', 'x,y')
# pt = Point(1,-4)
# print(pt)
# print(pt.x, pt.y)


# from collections import OrderedDict
# order_dict = OrderedDict()
# order_dict = {}
# 
# order_dict['b'] = 2
# order_dict['c'] = 3
# order_dict['d'] = 4
# order_dict['a'] = 1
# print(order_dict)


# from collections import defaultdict
# d = defaultdict(int)
# d ['a'] = 1
# d ['b'] = 2
# print(d)
# print(d['a'])
# print(d['b'])


from collections import deque
d = deque()

d.append(1)
d.append(2)

d.appendleft(3)
print(d)

# pop() , popleft() , popright(), clear()
# d.popleft()
d.extendleft([4,5,6])
print(d)

# d.rotate(1)
# print(d)
d.rotate(2)
print(d)