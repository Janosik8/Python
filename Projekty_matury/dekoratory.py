def decorator(func):
    def wrapper():
        print("-------------")
        func()
        print("-------------")
    return  wrapper()


def hello():
    print("Hello World")

decorator(hello)

@decorator
def jol():
    print("koldasdas")

