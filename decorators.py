
print("++++++Decoraters+++++++")
def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before execution")
        a = func(*args, **kwargs)
        print("after execution")
        return a
    return inner1    




@hello_decorator
def sum_of_two_numbers(a, b, c):
    print("inside the funtion")
    return a + b + c
print("Sum=", sum_of_two_numbers(5, 3, 7))    

