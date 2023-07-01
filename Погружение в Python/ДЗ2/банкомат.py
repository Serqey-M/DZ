# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

MULTIPLICITY = 50
PERCENTAGE_FOR_WITHDRAWAL = 0.015
MIN_PERCENTAGE_FOR_WITHDRAWAL = 30
MFX_PERCENTAGE_FOR_WITHDRAWAL = 600
MAX_COUNT_OPERATION = 3
ACCRUAL_PERCENTAGE = 0.03
WEALTH_TAX = 0.1
BORDER_WEALTH_TAX = 5_000_000


def replenish():
    with open("balance.txt", "r") as file:
        balance = float(file.read())
    if balance > BORDER_WEALTH_TAX:
        balance = balance - balance * WEALTH_TAX
    with open("count_operation.txt", "r") as file:
        count_operation = int(file.read())
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
    with open("balance.txt", "w") as file:
        file.write(str(balance))
    with open("count_operation.txt", "w") as file:
        file.write(str(count_operation))
    print(balance)


def withdraw():
    with open("balance.txt", "r") as file:
        balance = float(file.read())
    if balance > BORDER_WEALTH_TAX:
        balance = balance - balance * WEALTH_TAX
    with open("count_operation.txt", "r") as file:
        count_operation = int(file.read())
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
    with open("balance.txt", "w") as file:
        file.write(str(balance))
    with open("count_operation.txt", "w") as file:
        file.write(str(count_operation))
    print(balance)


def operation_selection():
    operation = -1
    while operation != 0:
        operation = int(
            input("Выберите операцию: 1 - пополнение; 2 - снятие; 0 - выход ")
        )
        match operation:
            case 1:
                replenish()
            case 2:
                withdraw()
            case 0:
                break
            case _:
                print("Не коректный выбор операции")


operation_selection()
