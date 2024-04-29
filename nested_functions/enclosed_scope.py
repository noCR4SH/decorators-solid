def make_multiplier(factor):
    def multiply(number):
        return number * factor
    
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))