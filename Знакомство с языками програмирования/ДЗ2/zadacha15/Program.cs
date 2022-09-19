// Задача 15: Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
Console.Write("Введите день недели: ");
string day = Console.ReadLine();
Console.Clear();
if(day=="6"||day=="7"|| day.ToLower() =="суббота"||day.ToLower() =="воскресенье")
{
   Console.WriteLine(day+" -> да"); 
}
else
{
    if(day=="1"||day=="2"||day=="3"||day=="4"||day=="5"||day.ToLower()=="понедельник"||day.ToLower()=="вторник"||day.ToLower()=="среда"||day.ToLower()=="четверг"||day.ToLower()=="пятница")
{
    Console.WriteLine(day+" -> нет");
}
else
{
    Console.WriteLine(day+" -> нет такого дня недели");
}}