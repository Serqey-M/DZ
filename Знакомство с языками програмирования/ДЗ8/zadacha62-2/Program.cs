// Задача 62. Напишите программу, которая заполнит спирально массив size на size.
Console.Clear();
int size = 10;
int number = 1;
int max_number = (size*size);
int position = 1;
int x=1, y=1;
Console.SetCursorPosition(x,y);
while(number<=max_number)
{
while(position<size) 
   {
    Console.Write(number);
    number++;
    position++;
    x+=3;
    Console.SetCursorPosition(x,y);
   }
while(position<2*size-1) 
   {
    Console.Write(number);
    number++;
    position++;
    y++;
    Console.SetCursorPosition(x,y);
   }
 while(position<3*size-2) 
   {
    Console.Write(number);
    number++;
    position++;
    x=x-3;
    Console.SetCursorPosition(x,y);
   }
while(position<4*size-4) 
   {
    Console.Write(number);
    number++;
    position++;
    y=y-1;
    Console.SetCursorPosition(x,y);
   }
Console.Write(number);
number++;
position=1;
size=size-2;
x=x+3;
    Console.SetCursorPosition(x,y);
}
