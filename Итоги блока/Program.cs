// Задача: Написать программу, которая из имеющегося массива строк формирует новый массив из строк, длина которых меньше, либо равна 3 символам. 
// Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения алгоритма. 
// При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.
string[] array = new string[0];
string end = "0";
for (int i = 0; end!="N"; i++)
{
    Console.Write($"Введите значение {i + 1} элемента массива, либо введите N чтобы завершить ввод: ");
    end=Console.ReadLine();
    if(end!="N")
    {
    Array.Resize(ref array, array.Length + 1); ;
    array[i]=end;
    }
}
string[] newArray = new string[0];
for (int i = 0; i < array.Length; i++)
{
    if (array[i].Length <= 3)
    {

        Array.Resize(ref newArray, newArray.Length + 1); ;
        newArray[newArray.Length - 1] = array[i];
    }
}
Console.Clear();
Console.WriteLine($"['{string.Join("','", array)}'] -> ['{string.Join("','", newArray)}']");