// Задача 52. Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце.
Console.Clear();
Random random = new Random();
int[,] matrix = new int[random.Next(2, 11), random.Next(2, 11)];
for (int i = 0; i < matrix.GetLength(0); i++)
{
    for (int j = 0; j < matrix.GetLength(1); j++)
    {
        matrix[i, j] = random.Next(-99, 100);
        Console.Write(matrix[i, j] + "\t");
    }
    Console.WriteLine();
}
Console.Write("Среднее арифметическое каждого столбца: ");
for (int j = 0; j < matrix.GetLength(1); j++)
{
    double sum = 0;
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        sum+= matrix[i, j];
    }
    Console.Write(Math.Round(sum/matrix.GetLength(0),1) + "; ");
}
