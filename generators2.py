def fabionacci(limit):
    #  0 1 1 2 3 5 8 13 21 ....
    
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fabionacci(30)
for i in fib:
    print(i)
    

# mygenerator = (i for i in range(30) if i % 2 == 0)
# for i in mygenerator:
#     print(i)

