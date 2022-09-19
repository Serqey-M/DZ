// Задача 68: Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.
Console.Write("Введите неотрицательное число m: ");
int m = Convert.ToInt32(Console.ReadLine());
while (m < 0)
{
    Console.Write("Введите неотрицательное число m: ");
    m = Convert.ToInt32(Console.ReadLine());
}
Console.Write("Введите неотрицательное число n: ");
int n = Convert.ToInt32(Console.ReadLine());
while (n < 0)
{
    Console.Write("Введите неотрицательное число n: ");
    n = Convert.ToInt32(Console.ReadLine());
}
int AckermanFunction(int m, int n)
{
    if (m == 0)
    {
        return n + 1;
    }
    else
    {
        if (n == 0)
        {
            return AckermanFunction(m - 1, 1);
        }
        else
        {
            return AckermanFunction(m - 1, AckermanFunction(m, n - 1));
        }
    }
}
Console.Clear();
Console.Write($"m = {m}, n = {n} -> A(m,n) = {AckermanFunction(m, n)}");