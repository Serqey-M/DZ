// Задача 25: Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.

Console.Write("Введите число А: ");
int numberA = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите число положительное число B: ");
int numberB = Convert.ToInt32(Console.ReadLine());
while(numberB<1)
{
    Console.Write("Введите число положительное число B: ");
   numberB = Convert.ToInt32(Console.ReadLine());
 }
int Rezalt = Pow(numberA,numberB);
Console.Clear();
Console.Write(numberA+", "+numberB+", -> "+Rezalt);

int Pow(int A, int B)
{
    int Rezult=A;
for(int index=1; index<B; index++)
{
     Rezult*=A;
}
return Rezult;
}