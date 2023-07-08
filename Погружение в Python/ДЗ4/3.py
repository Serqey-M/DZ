# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.

import datetime

MULTIPLICITY = 50
PERCENTAGE_FOR_WITHDRAWAL = 0.015
MIN_PERCENTAGE_FOR_WITHDRAWAL = 30
MFX_PERCENTAGE_FOR_WITHDRAWAL = 600
MAX_COUNT_OPERATION = 3
ACCRUAL_PERCENTAGE = 0.03
WEALTH_TAX = 0.1
BORDER_WEALTH_TAX = 5_000_000


def replenish():
    with open("balance.txt", "r", encoding='utf-8') as f1, \
         open("count_operation.txt", "r", encoding='utf-8') as f2:
        balance = float(f1.read())
        count_operation = int(f2.read())
    if balance > BORDER_WEALTH_TAX:
        balance = balance - balance * WEALTH_TAX
    summa = int(
        input("Введите сумму пополнения кратную 50 или 0 для отмены операции: ")
    )
    while summa % MULTIPLICITY != 0:
        summa = int(
            input("Введите сумму пополнения кратную 50 или 0 для отмены операции: ")
        )
    if summa != 0:
        balance += summa
        count_operation += 1
        if count_operation == MAX_COUNT_OPERATION:
            count_operation = 0
            balance *= 1 + ACCRUAL_PERCENTAGE
    data = [str(datetime.datetime.now()), f'Сумма пополнения: {summa}', f'Баланс: {balance}']
    with open("balance.txt", "w", encoding='utf-8') as f1, \
         open("count_operation.txt", "w", encoding='utf-8') as f2, \
         open("information.txt", "a", encoding='utf-8') as f3:
        f1.write(str(balance))
        f2.write(str(count_operation))
        f3.write(f'{str(data)} \n')
    print (f'Баланс: {balance}')


def withdraw():
    with open("balance.txt", "r", encoding='utf-8') as f1, \
         open("count_operation.txt", "r", encoding='utf-8') as f2:
        balance = float(f1.read())
        count_operation = int(f2.read())
    if balance > BORDER_WEALTH_TAX:
        balance = balance - balance * WEALTH_TAX
    summa = int(input("Введите сумму снятия кратную 50 или 0 для отмены операции: "))
    while summa % MULTIPLICITY != 0:
        summa = int(
            input("Введите сумму пополнения кратную 50 или 0 для отмены операции: ")
        )
    if summa != 0:
        summa_percentage_for_withdrawal = summa * PERCENTAGE_FOR_WITHDRAWAL
        if summa_percentage_for_withdrawal > MFX_PERCENTAGE_FOR_WITHDRAWAL:
            summa_percentage_for_withdrawal = MFX_PERCENTAGE_FOR_WITHDRAWAL
        elif summa_percentage_for_withdrawal < MIN_PERCENTAGE_FOR_WITHDRAWAL:
            summa_percentage_for_withdrawal = MIN_PERCENTAGE_FOR_WITHDRAWAL
        summa_withdrawals = summa + summa_percentage_for_withdrawal
        if summa_withdrawals <= balance:
            balance = balance - summa_withdrawals
        else:
            print("на счете не достаточно средств")
        count_operation += 1
        if count_operation == MAX_COUNT_OPERATION:
            count_operation = 0
            balance *= 1 + ACCRUAL_PERCENTAGE
    data = [str(datetime.datetime.now()), f'Сумма снятия: {summa}', f'Баланс: {balance}']
    with open("balance.txt", "w", encoding='utf-8') as f1, \
         open("count_operation.txt", "w", encoding='utf-8') as f2,\
         open("information.txt", "a", encoding='utf-8') as f3:
        f1.write(str(balance))
        f2.write(str(count_operation))
        f3.write(f'{str(data)} \n')
    print (f'Баланс: {balance}')


def operation_selection():
    operation = -1
    while operation != 0:
        operation = int(
            input("Выберите операцию: 1 - пополнение; 2 - снятие; 3 - информация; 0 - выход ")
        )
        match operation:
            case 1:
                replenish()
            case 2:
                withdraw()
            case 3:
                with open("information.txt", "r", encoding='utf-8') as f:
                   print(list(f))
            case 0:
                break
            case _:
                print("Не коректный выбор операции")


if __name__ == '__main__':
    operation_selection()