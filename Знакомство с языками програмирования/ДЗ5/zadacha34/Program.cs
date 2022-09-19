// Задача 34: Задайте массив заполненный случайными положительными трёхзначными числами. Напишите программу, которая покажет количество чётных чисел в массиве.
int [] array = new int[new Random().Next(3,21)];
for(int i=0; i<array.Length;i++)
{
    array[i]=new Random().Next(100, 1000);
}
int count=0;
for(int index=0;index<array.Length;index++)
{
if(array[index]%2==0)
{
    count++;
}
}
Console.Clear();
Console.Write("[{0}]",String.Join(", ",array));
Console.WriteLine(" -> "+ count);