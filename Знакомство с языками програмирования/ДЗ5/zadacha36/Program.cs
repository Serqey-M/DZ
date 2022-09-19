// Задача 36: Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих на нечётных позициях.
int [] array = new int[new Random().Next(3,21)];
for(int i=0; i<array.Length;i++)
{
    array[i]=new Random().Next(-99,100);
}
int sum=0;
for(int index=0;index<array.Length;index+=2)
{
    sum+=array[index];
}
Console.Clear();
Console.Write("[{0}]",String.Join(", ",array));
Console.WriteLine(" -> "+ sum);

