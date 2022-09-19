// Задача 27: Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.
Console.Write("Введите А: ");
int number = Convert.ToInt32(Console.ReadLine());
Console.Clear();
Console.Write(number+" -> "+ sum_number(number));

int sum_number(int number)
{
string number1 = Convert.ToString(Math.Abs(number));
int [] array = new int[number1.Length];
int Length = number1.Length;
for (int index=0; index<Length;index++)
{
array[index]=Convert.ToInt32(Convert.ToString(number1[index]));
}
if(number<0)
{
   array[0]=Convert.ToInt32(Convert.ToString(number1[0]))*-1; 
}
int sum = 0;
for(int index=0; index<Length;index++)
{
sum+=array[index];
}
return sum;
}