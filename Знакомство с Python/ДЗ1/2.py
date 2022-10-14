# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def Disjunction(x, y):
    if x == 0 and y == 0:
        return 0
    else:
        return 1


def Conjunction(x, y):
    if x == 1 and y == 1:
        return 1
    else:
        return 0


def Negation(x):
    if x == 0:
        return 1
    else:
        return 0


print('Введите значение X (1 или 0):')
X = input()
while X != '1' and X != '0':
    print('Введите значение X (1 или 0):')
    X = input()
print('Введите значение Y (1 или 0):')
Y = input()
while Y != '1' and Y != '0':
    print('Введите значение Y (1 или 0):')
    Y = input()
print('Введите значение Z (1 или 0):')
Z = input()
while Z != '1' and Z != '0':
    print('Введите значение Z (1 или 0):')
    Z = input()
step_1_left = Disjunction(X, Y)
step_2_left = Disjunction(step_1_left, Z)
step_3_left = Negation(step_2_left)
step_1_right = Negation(X)
step_2_right = Negation(Y)
step_3_right = Negation(Z)
step_4_right = Conjunction(step_1_right, step_2_right)
step_5_right = Conjunction(step_4_right, step_3_right)
print(step_3_left == step_5_right)
