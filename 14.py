try:
    a = int(input("ënter first number: "))
    b = int(input("ënter second number: "))
    print (a / b)
    r = open("file_not_exists.txt")
except ZeroDivisionError:
    print("could not be divided by zero")
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print(e.args)
# except Exception as e:
#     print("Something went Wrong {}".format(e.args))
print("blablabl")
