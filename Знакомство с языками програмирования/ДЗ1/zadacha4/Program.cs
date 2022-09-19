// Задача 4: Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел.
Console.Write("Введите число 1: ");
double number1 = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите число 2: ");
double number2 = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите число 3: ");
double number3 = Convert.ToInt32(Console.ReadLine());
Console.Clear();
Console.Write(number1);
Console.Write(" ");
Console.Write(number2);
Console.Write(" ");
Console.Write(number3);
Console.Write(" -> ");
if(number1>number2)
{
    if(number1>number3)
    {
       Console.Write(number1); 
    }
    else
    {
        Console.Write(number3); 
    }
}
else
{
    if(number2>number3)
    {
       Console.Write(number2); 
    }
    else
    {
        Console.Write(number3); 
    }
}
