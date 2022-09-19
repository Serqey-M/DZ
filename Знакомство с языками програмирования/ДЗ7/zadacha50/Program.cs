// Задача 50. Напишите программу, которая на вход принимает позиции элемента в двумерном массиве, и возвращает значение этого элемента или же указание, что такого элемента нет.
Console.Write("Введите номер строки: ");
int rows = Convert.ToInt32(Console.ReadLine());
while (rows < 1)
{
    Console.Write("Введите номер строки: ");
    rows = Convert.ToInt32(Console.ReadLine());
}
Console.Write("Введите номер столбца: ");
int columns = Convert.ToInt32(Console.ReadLine());
while (columns < 1)
{
    Console.Write("Введите номер столбца: ");
    columns = Convert.ToInt32(Console.ReadLine());
}
Console.Clear();
Random random = new Random();
double[,] matrix = new double[random.Next(2, 11), random.Next(2, 11)];
for (int i = 0; i < matrix.GetLength(0); i++)
{
    for (int j = 0; j < matrix.GetLength(1); j++)
    {
        matrix[i, j] = random.Next(-99, 100) + Math.Round(random.NextDouble(), 2);
        Console.Write(matrix[i, j] + "\t");
    }
    Console.WriteLine();
}
if (rows > matrix.GetLength(0) || columns > matrix.GetLength(1))
    Console.WriteLine($"{rows},{columns} -> такого числа в массиве нет");
else
    Console.Write($"{rows},{columns} -> {matrix[rows - 1, columns - 1]}");