import functools

# def start_end_decorator(func):  
    
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         # Do ...
#         # print("Start") 
#         result = func(*args, **kwargs)
#         # Do ...
#         # print("End")
#         return result
#     return wrapper

# @start_end_decorator
# def add5(x):
#     return x + 5
# 
# print(help(add5))
# print(add5.__name__)

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')
    
greet('Alex')