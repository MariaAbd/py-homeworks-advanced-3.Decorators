import datetime
from pprint import pprint


def path_dec(path):
    def print_decorator(old_func):
        def new_func(*args, **kwargs):
            name = old_func.__name__
            start_time = str(datetime.datetime.now())
            result = old_func(*args, **kwargs)
            print('Вызвана функция', name, 'в', start_time)
            print(f'С аргументами {args}')
            print('Получен результат', result)
            try:
                with open(path, mode='w') as file:
                    file.write(str([name, start_time, result]))
                    return result
            except FileNotFoundError:
                print('Файла не существует')

        return new_func
    return print_decorator


dishes = []
cook_book = {}

path_recipe = path_dec('dec_1.txt')


@path_recipe
def get_data(file_name):
    n = 0
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            dishes.append(line.strip())
            cook_book[dishes[n]] = []
            ingredients = int(file.readline())
            for line_ingredients in range(ingredients):
                ing_list = []
                dish = {}
                for word in file.readline().split(' | '):
                    ing_list.append(word)
                dish["ingredient_name"] = ing_list[0]
                dish["quantity"] = ing_list[1]
                dish["measure"] = ing_list[2]
                cook_book[dishes[n]].append(dish)
            n += 1
            file.readline().strip()
    return cook_book


result_ = get_data('recipes.txt')
pprint(result_)
