# my_file = open("url.txt")
# for line in my_file.readlines():
#     print(line,end='')
from u11 import url_caller

def get_names():
    my_file = open("nams.txt", "w")
    for i in range(5):
        current_name = input("ënter your name")
        my_file.write(f"{current_name}\n")
    my_file.close()

def print_name():
    my_file = open("nams.txt","r")
    for line in my_file.readlines():
        print(f"Hello {line}",end='')
    my_file.close()


def get_urls():
    url_file = open("url.txt","r")
    for line in url_file.readlines():
        url_caller(line.strip())
    url_file.close()

def show_names():
    with open("url.txt") as my_file_name:
        for line in my_file_name.readlines():
            print(f"hello {url_caller(line.strip())}",end='')

# get_names()
# print_name()
get_urls()
show_names()