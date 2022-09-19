// Задача 10: Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа.
 Console.Write("Введите трехзначное число: ");
int num = Convert.ToInt32(Console.ReadLine());
while(Math.Abs(num)<100 ||Math.Abs(num)>999)
{
    Console.WriteLine("Введите трехзначное число");
    num = Convert.ToInt32(Console.ReadLine());
 }
Console.Clear();
Console.WriteLine(num+" -> "+Math.Abs(num)%100/10);