from datetime import datetime
def my_decorator(func):
    def wrapper():
        print("something {}".format(datetime.now()))
        func()
        print("ëlse")

    return wrapper

@my_decorator
def say_whee():
    print("whee")

say_whee()