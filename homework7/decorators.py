import timeit

def cancel(func):
    def wrapper():
        print("Method {}:".format(func))
        raise Exception("Method canceled!")
        func()
    return wrapper

def function_speed(func):
    def wrapper():
        t1 = time.time()
        res = func()
        t2 = time.time()
        return (t2 - t1), res
    return wrapper


def count_execution(func):
    pass


def catch(func):
    try:
        func()
    except Exception as e:
        print(e)

@cansel
decorating_function():
    print('something')

some = decorating_function()
