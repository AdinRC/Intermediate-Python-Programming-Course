# String: ordered, imutable, text representation

# my_string = "Hello world"
# char = my_string[0]
# print (char)


# greeting = "Hello"
# name = "Tom"
# sentence = greeting + " " + name
# print (sentence)
# 
# for i in greeting:
#     print (i)
# 
# if "e" in greeting:
#     print ("Yes")
# else:
#     print ("No")


# my_string = "     Hello world     "
# my_string = my_string.strip()
# print (my_string)


# my_string = "Hello world"
# print (my_string.upper)
# print (my_string.lower)
# print (my_string.startswith("Hello")
# print (my_string.startswith("World")
# print (my_string.endswith("Hello")
# print (my_string.endswith("World")
# print (my_string.find("o")
# print (my_string.count("o")
# print (my_string.replace("World", "Universe")
# print (my_string.lower)


# my_string = 'how,are,you,doing'
# my_list = my_string.split(",")
# print(my_list)
# new_string = ' '.join(my_list)
# print(new_string)

# from timeit import default_timer as timer
# my_list = ['a'] * 600000
# # print(my_list)
# 
## bad
# start = timer()
# my_string = ''
# for i in my_list:
#     my_string += i
# stop = timer()
# print(stop-start)
# 
## good
# start = timer()
# my_string = ''.join(my_list)
# stop = timer()
# print(stop-start)


# %, .format(), f-string

# var = "Tom"
# my_string = "The variable is %s" % var
# print(my_string)

var = 3.12567
var2 = 6
# my_string = "The variable is %d" % var
# print(my_string)
# my_string = "The variable is %.3f" % var
# print(my_string)
# 
# my_string = "The variable is {}".format(var)
# print(my_string)
# my_string = "The variable is {:.2f} and {}".format(var,var2)
# print(my_string)
my_string = f"The variable is {var} and {var2}"
print(my_string)
my_string = f"The variable is {var*2} and {var2}"
print(my_string)
my_string = f"The variable is {var:.2f} and {var2}"
print(my_string)