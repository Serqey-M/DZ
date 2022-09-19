// Задача 2: Напишите программу, которая на вход принимает два числа и выдаёт, какое число большее, а какое меньшее.
Console.Write("Введите число a: ");
double number_a = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите число b: ");
double number_b = Convert.ToInt32(Console.ReadLine());
Console.Clear();
Console.Write("a = ");
Console.Write(number_a);
Console.Write("; b = ");
Console.Write(number_b);
Console.Write(" -> ");
if(number_a>number_b)
{
    Console.Write("max = ");
    Console.Write(number_a);
}
else
{
    Console.Write("max = ");
    Console.Write(number_b);
}