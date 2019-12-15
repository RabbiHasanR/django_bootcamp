# def hello():
#     return 'Hi rabbi'
#
# def other(func):
#     print('hello')
#     print(func())
#
# other(hello)

def new_decorator(func):

    def wrap_func():
        print('Code here before executing func!')
        func()
        print('func() has been called')
    return wrap_func()
@new_decorator
def func_need_decorator():
    print('this function need of a decorator!')

func_need_decorator
