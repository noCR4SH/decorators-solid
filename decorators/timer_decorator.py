import time

def timer(func):
    # Wrapper takes unlimited number of arguments and key-value arguments
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter() # taking current time
        result = func(*args, **kwargs) # passing all arguments to decorated function
        end_time = time.perf_counter() # current time after running the function
        print(f"{func.__name__} ran in: {end_time - start_time} seconds")
        return result
    return wrapper

@timer
def multiply(x, y):
    return x * y

print(multiply(5, 3))