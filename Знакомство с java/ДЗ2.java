
// 1. Напишите программу, чтобы найти вхождение в строке (содержащей все символы другой строки).
// 2. Напишите программу, чтобы проверить, являются ли две данные строки вращением друг друга (вхождение в обратном порядке).
// 3. *Напишите программу, чтобы перевернуть строку с помощью рекурсии.
// 4. Дано два числа, например 3 и 56, необходимо составить следующие строки: 3 + 56 = 59 3 – 56 = -53 3 * 56 = 168 Используем метод StringBuilder.append().
// 5. Замените символ “=” на слово “равно”. Используйте методы StringBuilder.insert(),StringBuilder.deleteCharAt().
// 6. *Замените символ “=” на слово “равно”. Используйте методы StringBuilder.replace().
// 7. **Сравнить время выполнения пунка 6 со строкой содержащей 10000 символов "=" средствами String и StringBuilder.
import java.util.Random;

public class ДЗ2 {
    public static void main(String[] args) {
        String st1 = new String("Hello world");
        String st2 = new String("dlrow olleh");
        int n1 = 3;
        int n2 = 56;
        String str3 = generating_string("+", "=", 10000);
        StringBuilder str4 = new StringBuilder(str3);
        // 1.
        System.out.println("Задание 1");
        entry(st1, st2);
        // 2.
        System.out.println("Задание 2");
        rotation(st1, st2);
        // 3.
        System.out.println("Задание 3");
        System.out.println(reverseString(st1));
        // 4.
        System.out.println("Задание 4");
        System.out.println(stringBuilderappend(n1, n2, "+"));
        System.out.println(stringBuilderappend(n1, n2, "-"));
        System.out.println(stringBuilderappend(n1, n2, "*"));
        // 5.
        System.out.println("Задание 5");
        System.out.println(replace_character_1(stringBuilderappend(n1, n2,
                "+").toString(), "=", "равно"));
        // 6.
        System.out.println("Задание 6");
        System.out.println(replace_character_2(stringBuilderappend(n1, n2,
                "-").toString(), "=", "равно"));
        // 7.
        System.out.println("Задание 7");
        double beginning = System.currentTimeMillis();
        String_replace(str3, "=", "равно");
        System.out.println(System.currentTimeMillis() - beginning);
        beginning = System.currentTimeMillis();
        StringBuilder_replace(str4, "=", "равно");
        System.out.println(System.currentTimeMillis() - beginning);
    }

    public static void entry(String str1, String str2) {
        if (str1.contains(str2)) {
            System.out.println("строка 2 входит в строку 1");
        } else {
            System.out.println("строка 2 не входит в строку 1");
        }
    }

    public static void rotation(String str1, String str2) {
        String str3 = new StringBuilder(str2).reverse().toString();
        if (str3.equalsIgnoreCase(str1)) {
            System.out.println("строки являются вращением друг друга");
        } else {
            System.out.println("строки не являются вращением друг друга");
        }
    }

    public static String reverseString(String str) {

        int length = str.length();
        if (length <= 1) {
            return str;
        }
        String leftPart = str.substring(0, length / 2);
        String rightPart = str.substring(length / 2, length);
        return reverseString(rightPart) + reverseString(leftPart);
    }

    public static StringBuilder stringBuilderappend(int n1, int n2, String operator) {
        StringBuilder str = new StringBuilder();
        if (operator == "+") {
            str.append(n1).append(" ").append(operator).append(" ").append(n2).append(" = ").append(n1 + n2);
        } else if (operator == "-") {
            str.append(n1).append(" ").append(operator).append(" ").append(n2).append(" = ").append(n1 - n2);
        } else if (operator == "*") {
            str.append(n1).append(" ").append(operator).append(" ").append(n2).append(" = ").append(n1 * n2);
        } else if (operator == "/") {
            str.append(n1).append(" ").append(operator).append(" ").append(n2).append(" = ").append(n1 / n2);
        } else {
            str.append("Не известный оператор");
        }
        return str;
    }

    public static StringBuilder replace_character_1(String in_string, String replace, String on) {
        StringBuilder str = new StringBuilder(in_string);
        int index = str.indexOf(replace);
        str.deleteCharAt(index);
        str.insert(index, on);
        return str;
    }

    public static StringBuilder replace_character_2(String in_string, String replace, String on) {
        StringBuilder str = new StringBuilder(in_string);
        int index = str.indexOf(replace);
        str.replace(index, index + 1, on);
        return str;
    }

    public static String generating_string(String str1, String str2, int count) {
        String str = new String("");
        int c = 0;
        while (c < count) {
            if (new Random().nextInt(2) == 0) {
                str += str1;
            } else {
                str += str2;
                c++;
            }
        }
        return str;
    }

    public static String String_replace(String str, String str1, String str2) {
        String str3 = str.replace(str1, str2);
        return str3;
    }

    public static StringBuilder StringBuilder_replace(StringBuilder str, String str1, String str2) {
        int index = str.indexOf(str1);
        while (index != -1) {
            str.replace(index, index + str1.length(), str2);
            index += str2.length();
            index = str.indexOf(str1);
        }
        return str;
    }

}
