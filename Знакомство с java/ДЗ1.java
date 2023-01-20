// 1. Выбросить случайное целое число в диапазоне от 0 до 2000 и сохранить в i
// 2. Посчитать и сохранить в n номер старшего значащего бита выпавшего числа
// 3. Найти все кратные n числа в диапазоне от i до Short.MAX_VALUE сохранить в массив m1
// 4. Найти все некратные n числа в диапазоне от Short.MIN_VALUE до i и сохранить в массив m2
// Пункты реализовать в методе main
// *Пункты реализовать в разных методах

import java.util.Random;

public class ДЗ1 {
    // Реализация в методе main
    // public static void main(String[] args) {
        
    //     int i = new Random().nextInt(2000);
    //     int n = Integer.toBinaryString(i).length();
    //     int c = 0;
    //     for (int j = i; j < Short.MAX_VALUE; j++) {
    //         if (j % n == 0)
    //             c++;
    //     }
    //     int[] m1 = new int[c];
    //     c = 0;
    //     for (int j = i; j < Short.MAX_VALUE; j++) {
    //         if (j % n == 0)
    //             m1[c++] = j;
    //     }
    //     c = 0;
    //     for (int j = i; j > Short.MIN_VALUE; j--) {
    //         if (j % n != 0)
    //             c++;
    //     }
    //     int[] m2 = new int[c];
    //     c = 0;
    //     for (int j = i; j > Short.MIN_VALUE; j--) {
    //         if (j % n != 0)
    //             m2[c++] = j;
    //     }
    // }

    // Реализация в разных методах
    public static void main(String[] args) {
    }
    public static int Random() {
        return new Random().nextInt(2000);   
    }
    public static int number_highest_bit(int i) {
        return Integer.toBinaryString(i).length();
    }
    public static int[] multiples(int i, int n) {
        int c = 0;
        for (int j = i; j < Short.MAX_VALUE; j++) {
            if (j % n == 0)
                c++;
        }
        int[] m1 = new int[c];
        c = 0;
        for (int j = i; j < Short.MAX_VALUE; j++) {
            if (j % n == 0)
                m1[c++] = j;
        }
        return m1;
    }
    public static int[] non_multiples(int i, int n) {
        int c = 0;
        for (int j = i; j > Short.MIN_VALUE; j--) {
            if (j % n != 0)
                c++;
        }
        int[] m2 = new int[c];
        c = 0;
        for (int j = i; j > Short.MIN_VALUE; j--) {
            if (j % n != 0)
                m2[c++] = j;
        }
        return m2;
    }

}