# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
print ("Введите день недели: ")
day = input()
if day=="6"or day=="7" or day.lower() =="суббота" or day.lower() =="воскресенье":
    print(day , " -> да"); 
elif day=="1" or day=="2" or day=="3" or day=="4" or day=="5" or day.lower() == "понедельник" or day.lower() == "вторник" or day.lower() == "среда" or day.lower() == "четверг" or day.lower() == "пятница":
    print(day+" -> нет")
else:
    print(day+" -> нет такого дня недели")
