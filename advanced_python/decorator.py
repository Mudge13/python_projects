def my_decorator(fun):
    print("baba")

    def wrap(x):
        print("*******")
        fun(x)
        print("*******")
        print("hello world")
    return wrap


@my_decorator
def my_fun(greeting):
    print(f"hellooo {greeting}")


# my_decorator(my_fun)
my_fun("canada")  # automatically gives value to wrap()
# same as wrap() = my_decorator(my_fun)()
# so wrap(greeting) = my_decorator(my_fun)(greeting)
