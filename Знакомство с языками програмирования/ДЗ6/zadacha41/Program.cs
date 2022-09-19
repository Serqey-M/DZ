// Задача 41: Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь.
Console.WriteLine("Сколько чисел желаете ввести?");
int M = Convert.ToInt32(Console.ReadLine());
int[]array = new int[M];
 int count = 0;
 for (int i=0;i<M;i++)
 {
 Console.WriteLine("введите число: ");
 array[i]=Convert.ToInt32(Console.ReadLine());
 if(array[i]>0)
 {count++;}
 }
 Console.Clear();
 Console.WriteLine($"{string.Join(", ",array)} -> {count}");