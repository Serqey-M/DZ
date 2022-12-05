# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# 1. Определить корни
# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает
# 4. Построить график
# 5. Вычислить вершину
# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0

import math
from sympy.plotting import plot
from sympy import *

interval = [-10, 10]
roots = []
x = interval[0]
while x < interval[1]:
    f = (-12*x**4*math.sin(math.cos(x)) - 18*x**3+5*x**2 + 10*x - 30)
    x += 0.00001
    if round(f) == 0:
        roots.append(round(x, 1))
print(f'1. корни: {sorted(set(roots))}')
peak = []
ascending_descending_intervals = []
x = interval[0]
f1 = (-12*x**4*math.sin(math.cos(x)) - 18*x**3+5*x**2 + 10*x - 30)
x += 0.01
f2 = (-12*x**4*math.sin(math.cos(x)) - 18*x**3+5*x**2 + 10*x - 30)
if f1 > f2:
    sign = '-'
else:
    sign = '+'
while x < interval[1]:
    peak_n = []
    f1 = (-12*x**4*math.sin(math.cos(x)) - 18*x**3+5*x**2 + 10*x - 30)
    x += 0.01
    f2 = (-12*x**4*math.sin(math.cos(x)) - 18*x**3+5*x**2 + 10*x - 30)
    if sign == '-' and f1 < f2:
        peak_n.append(round(x, 2))
        peak_n.append(round(f1, 2))
        ascending_descending_intervals.append(round(x, 2))
        peak.append(peak_n)
    elif sign == '+' and f1 > f2:
        peak_n.append(round(x, 2))
        peak_n.append(round(f1, 2))
        ascending_descending_intervals.append(round(x, 2))
        peak.append(peak_n)
    if f1 > f2:
        sign = '-'
    else:
        sign = '+'
ascending_descending_intervals.append(interval[1])
ascending_descending_intervals.insert(0, interval[0])
function_decreasing = []
function_increases = []
for i in range(1, len(ascending_descending_intervals)):
    x = ascending_descending_intervals[i]
    f1 = (-12*x**4*math.sin(math.cos(x)) - 18*x**3+5*x**2 + 10*x - 30)
    x = ascending_descending_intervals[i-1]
    f2 = (-12*x**4*math.sin(math.cos(x)) - 18*x**3+5*x**2 + 10*x - 30)
    if f1 < f2:
        function_decreasing.append(
            f'от {ascending_descending_intervals[i-1]} до {ascending_descending_intervals[i]}')
    else:
        function_increases.append(
            f'от {ascending_descending_intervals[i-1]} до {ascending_descending_intervals[i]}')
print(f'2. функция возрастает на участках {function_increases}')
print(f'3. функция убывает на участках {function_decreasing}')
x = Symbol('x')
plot((-12*x**4*sin(cos(x)) - 18*x**3+5*x**2 + 10*x - 30,
     (x, interval[0], interval[1])), line_color='red')
print(f'5. вершины: {peak}')
positive_negative_intervals = sorted(set(roots))
positive_negative_intervals.append(interval[1])
positive_negative_intervals.insert(0, interval[0])
positive_function = []
negative_function = []
for i in range(1, len(positive_negative_intervals)):
    x = (positive_negative_intervals[i]+positive_negative_intervals[i-1])/2
    f1 = (-12*x**4*math.sin(math.cos(x)) - 18*x**3+5*x**2 + 10*x - 30)
    if f1 < 0:
        negative_function.append(
            f'от {positive_negative_intervals[i-1]} до {positive_negative_intervals[i]}')
    else:
        positive_function.append(
            f'от {positive_negative_intervals[i-1]} до {positive_negative_intervals[i]}')
print(f'6. f > 0 на участках {positive_function}')
print(f'7. f < 0 на участках {negative_function}')
