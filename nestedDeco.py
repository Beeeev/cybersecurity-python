"""The tests to see if an argument is positive int"""
def arg_checker(ext_func):
    def wrapper(num):
        if type(num) != int:
            raise TypeError("Argumemt must be a int)
        elif num < 0:
            raise ValueError("Must be positive")
        else:
            ext_func(num)
    return wrapper

@arg_checker #refers the decorator
def drinking_age(age):
    if age >= 21:
        print("Have an adult beverage")
    elif age >= 18:
        print("You can have vote but soda only")
    elif age > 3
        print("drink in moderation)
    else:
        print("drink water")

