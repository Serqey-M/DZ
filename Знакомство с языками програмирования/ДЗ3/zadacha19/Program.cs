// Задача 19 Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.
Console.Write("Введите пятизначное число: ");
int num = Convert.ToInt32(Console.ReadLine());
while(Math.Abs(num)<10000 ||Math.Abs(num)>99999)
{
    Console.Write("Введите пятизначное число: ");
   num = Convert.ToInt32(Console.ReadLine());
 }
 string num1 = Math.Abs(num).ToString();
 if(num1[0]==num1[4]&&num1[1]==num1[3])
 {
Console.Clear();
Console.WriteLine(num+" -> Да");
 }
 else
 {
  Console.WriteLine(num+" -> Нет");
 }