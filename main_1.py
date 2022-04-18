import datetime


def print_decorator(old_func):
    def new_func(*args, **kwargs):
        name = old_func.__name__
        start_time = str(datetime.datetime.now())
        result = old_func(*args, **kwargs)
        with open('dec.txt', mode='w') as file:
            file.write(str([name, start_time, result]))
            return f'Вызвана функция {name} в {start_time}', f'С аргументами {args}',\
                   f'Получен результат {result}'

    return new_func



@print_decorator
def foo(a, b):
    return a + b

print(foo(2, 5))


