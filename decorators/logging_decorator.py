# Decorator definition that takes a function as argument
def log_function_call(func):
    # Taking 2 arguments (x and y) and passes to decororated function; prints before and after calling the decorated function
    def wrapper(x, y):
        print(f"Calling {func.__name__} with {x} and {y}")
        result = func(x, y)
        print(f"Result: {result}")
        return result # returns the result of the decorated function
    return wrapper # returns decorated function

@log_function_call # decorating a function
def add(x, y):
    return x + y

result = add(2, 3)
print(result)