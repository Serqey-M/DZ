// Задача 23 Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.
Console.Write("Введите число: ");
int N = Convert.ToInt32(Console.ReadLine());
Console.Clear();
Console.Write(N+" -> ");
if(N>=1)
{for(int index=1;index<=N;index++)
{
    Console.Write(Math.Pow(index,3)+", ");
}}
else
{for(int index=0;index>=N;index=index-1)
{
    Console.Write(Math.Pow(index,3)+", ");
}}