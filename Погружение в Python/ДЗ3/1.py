# Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.

string = input('Введите строку: ')
symbols = set(i  for i in string if i.isalpha() == True)
dictionary = {}
for i in symbols:
    count_ = 0
    for j in string:
        if i == j:
            count_ += 1
    dictionary[i] = count_
print(f'Без метода count {dictionary}')

for i in symbols:
    dictionary[i] = string.count(i)
print(f'Метод count {dictionary}')
