// Задача 58: Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.
int[,] matrix (int m,int n)
{
int[,] matrix = new int[m, n];
for (int i = 0; i < m; i++)
{
    for (int j = 0; j < n; j++)
    {
        matrix[i, j] = new Random().Next(-99, 100);
        Console.Write(matrix[i, j] + "\t");
    }
    Console.WriteLine();
}
return matrix;
}

Console.Clear();
int m = new Random().Next(2,11);
int n = new Random().Next(2,11);
int c = new Random().Next(2,11);
Console.WriteLine("Матрица 1");
int[,] matrix1 = matrix(m,n);
Console.WriteLine("Матрица 2");
int[,] matrix2 = matrix(n,c);
Console.WriteLine("Произведение матриц");
int [,] matrix3 = new int[m,c];
for (int i = 0; i < m; i++)
{
    for (int j = 0; j < c; j++)
    {
        int sum = 0;
        for (int k=0;k<n;k++)
        {
            sum += matrix1[i,k]*matrix2[k,j];
        }
        matrix3[i, j] = sum;
        Console.Write(matrix3[i, j] + "\t");
    }
    Console.WriteLine();
}