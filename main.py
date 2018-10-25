from functools import wraps


def my_decorator_0(f):
    '''This is Docstring decorator_0'''
    def wrapper(*args, **kwargs):
        print('call wrapper')
        return f(*args, **kwargs)
    return wrapper

def my_decorator_1(f):
    '''This is Docstring decorator_1'''
    @wraps(f)
    def wrapper(*args, **kwargs):
        print('call wrapper')
        return f(*args, **kwargs)
    return wrapper



@my_decorator_0
def example_0():
    '''This is Docstring example_0'''
    print('call example_0')

@my_decorator_1
def example_1():
    '''This is Docstring example_1'''
    print('call example_1')


print('-- without wraps')
example_0()
print(example_0.__name__)
print(example_0.__doc__)

print('\n')

print('-- with wraps')
example_1()
print(example_1.__name__)
print(example_1.__doc__)
