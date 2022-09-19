// Задача 13: Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.
Console.Write("Введите число: ");
int number = Convert.ToInt32(Console.ReadLine());
Console.Clear();
if(Math.Abs(number)<100)
{
    Console.WriteLine(number+" -> третьей цифры нет");
}
else
{
string num = Math.Abs(number).ToString();
int[] array = new int[num.Length];
int length = num.Length;
int index = 0;
while(index<length)
{
    array[index]=int.Parse(num[index].ToString());
    index++;
}
Console.WriteLine(number+" -> "+array[2]);
}