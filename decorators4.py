
class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0
        
    def __call__(self, *args, **kwargs):
        # print("Hi There")
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)
    
    
# cc = CountCalls(None)
# cc()
        
@CountCalls
def say_hello():
    print ("Hello")
    
say_hello()