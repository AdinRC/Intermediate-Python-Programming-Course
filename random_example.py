import random

# a = random.random()
# a = random.uniform(1, 10)
# a = random.randint(1, 10)
# a = random.randrange(1, 10)
# a = random.normalvariate(0, 1)
# print (a)


# mylist = list("ABCDEFGH")
# 
# a = random.choice(mylist)
# a = random.sample(mylist, 3)
# a = random.choices(mylist, k=3)
# print (a)
# 
# random.shuffle(mylist)
# print (mylist)


random.seed(1)
print (random.random())
print (random.randint(1, 10))
random.seed(2)
print (random.random())
print (random.randint(1, 10))

random.seed(1)
print (random.random())
print (random.randint(1, 10))
random.seed(2)
print (random.random())
print (random.randint(1, 10))