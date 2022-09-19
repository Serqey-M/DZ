// Задача 38: Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.
double [] array = new double[new Random().Next(3,20)];
for(int i=0; i<array.Length;i++)
{
    array[i]=Math.Round(new Random().NextDouble(),2) + new Random().Next(-99,100);
}
double max = array[0];
double min = array[0];
for(int i=1; i<array.Length;i++)
{
if(array[i]>max)
{
    max=array[i];
}
else
{
    if(array[i]<min)
    {
        min=array[i];
    }
}
}
double result = max-min;
Console.Clear();
Console.Write("[{0}]",String.Join("  ",array));
Console.WriteLine(" -> "+ result);