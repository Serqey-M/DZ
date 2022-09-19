// Задача 13: Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.
Console.Write("Введите число: ");
int num = Convert.ToInt32(Console.ReadLine());
int num1 = Math.Abs(num);
int digit = 0;
Console.Clear();
if(Math.Abs(num)<100)
{
    Console.WriteLine(num+" -> третьей цифры нет");
}
else
{
    while(num1>=100)
{
    num1=num1/10;
    digit++;
}
Console.WriteLine(num+" -> "+Math.Floor(Math.Abs(num)%Math.Pow(10,digit)/Math.Pow(10,digit-1)));
}