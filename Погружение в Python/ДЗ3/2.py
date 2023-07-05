# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

dictionary = {
    'Иван': ('рюкзак', 'палатка', 'огниво', 'фонарик','аптечка'), 
    'Сергей': ('рюкзак', 'спички','аптечка','палатка','термос'), 
    'Антон':('рюкзак', 'зажигалка', 'палатка', 'фонарик', 'термос')
    }
list_of_things_0 = []
for i in dictionary:
    list_of_things_0.extend(dictionary[i])
list_of_things = set(list_of_things_0)
list_x = []
list_y = {}
list_z = {}
for i in list_of_things:
    count_ =  list_of_things_0.count(i)
    if count_ == len(dictionary):
        list_x.append(i)
    elif count_ == 1:
        for j in dictionary:
            if i in dictionary[j]:
                list_y.update({i:j})
    elif count_ == len(dictionary)-1:
        for j in dictionary:
            if i not in dictionary[j]:
                list_z.update({i:j})
print(f'Какие вещи взяли все три друга: {list_x}')      
print(f'Какие вещи уникальны, есть только у одного друга: {list_y}') 
print(f'Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует: {list_z}')