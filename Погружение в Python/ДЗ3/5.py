# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.

list_of_things = {'палатка':3, 'фонарь':1.5, 'аптечка':1, 'зажигалка':0.015, 'термос':0.7, 'котелок':0.8, 'топор': 0.6, 'нож':0.1, 'Столовые приборы':0.25, 'еда':1.2}
backpack_capacity = float(input('Введите грузоподъемность рюкзака: '))
backpack_weight = 0
contents_backpack = []
for i, j in list_of_things.items():
    if backpack_weight + j <= backpack_capacity:
        backpack_weight += j
        contents_backpack.append(i)
print(f'Наполнение рюкзака: {contents_backpack}, вес: {backpack_weight}')

'''*Все возможные варианты комплектации рюкзака'''

# sorted_list_of_things = sorted(list_of_things.items(), key=lambda x: x[1], reverse=True)
# print((sorted_list_of_things))
# for i in range(len(sorted_list_of_things)):
#     for items, weight  in dict(sorted_list_of_things).items():
#         if backpack_weight + weight <= backpack_capacity:
#             backpack_weight += weight
#             contents_backpack.append(items)
#     print(f'{i+1}. Наполнение рюкзака: {contents_backpack}, вес: {backpack_weight}')
#     sorted_list_of_things.append(sorted_list_of_things[0])
#     sorted_list_of_things.pop(0)
#     backpack_weight = 0
#     contents_backpack = []
