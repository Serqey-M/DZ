// Задача 29: Напишите программу, которая задаёт массив из 8 элементов и выводит их на экран.
void array(int size)
{
int [] array = new int[size];
for(int index=0; index<size;index++)
{
    array[index]= new Random().Next(-99,100);
    Console.Write(array[index]+", ");
}
}
Console.Clear();
array(8);