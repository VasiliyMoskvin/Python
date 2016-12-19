import time

def time_it(func):
    def decorated(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print("Функция {} работала {}".format(func.__name__, time.time() - start))
        return res
    return decorated

@time_it
def my_func():
    i = 0
    while i<10000000:
        i += 1

def my_func_2():
    start = time.time()
    i = 0
    while i<10000000:
        i += 1
    print("Функция {} работала {}".format(__name__, time.time() - start))

my_func()
my_func_2()