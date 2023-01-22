import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Random;

// 1 Объявить два списка ArrayList, в каждый добавить по 20 случайных чисел. Удалить из первого списка элементы отсутствующие во втором списке.
//  Отсортировать первый список методом sort класса Collections.
// 2 * Отсортировать второй список методом sort списка и компаратором по уменьшению.
// 3 **Отсортировать первый список пузырьковой сортировкой самостоятельно, без использования доп методов и классов.

public class ДЗ3 {

    public static <T> void main(String[] args) {
        // 1.
        System.out.println("Задание 1");
        Random rnd = new Random();
        ArrayList<Integer> lst1 = new ArrayList<>();
        for (int i = 0; i < 20; i++) {
            lst1.add(rnd.nextInt(100));
        }
        System.out.println("Список 1:" + lst1);

        ArrayList<Integer> lst2 = new ArrayList<>();
        for (int i = 0; i < 20; i++) {
            lst2.add(rnd.nextInt(100));
        }
        System.out.println("Список 2:" + lst2);
        ArrayList<Integer> copy_lst1 = new ArrayList<>(lst1);
        copy_lst1.retainAll(lst2);
        System.out.println("Cписок 1 с удаленными элементами отсутствующими в списке 2:" + copy_lst1);
        ArrayList<Integer> copy2_lst1 = new ArrayList<>(lst1);
        Collections.sort(copy2_lst1);
        System.out.println("Список 1 отсортированный методом sort класса Collections:" + copy2_lst1);
        // 2.
        System.out.println("Задание 2");
        lst2.sort(new Comparator<Integer>() {
            @Override
            public int compare(Integer t, Integer t1) {
                return t1 - t;
            }
        });
        System.out.println("Список 2 отсортированный методом sort списка и компаратором по уменьшению:" + lst2);
        // 3.
        System.out.println("Задание 3");
        ArrayList<Integer> copy3_lst1 = new ArrayList<>(lst1);

        for (int i = 0; i < copy3_lst1.size(); i++) {
            int max = copy3_lst1.get(i);
            int ind_max = i;
            for (int j = i + 1; j < copy3_lst1.size(); j++) {
                if (max < copy3_lst1.get(j)) {
                    max = copy3_lst1.get(j);
                    ind_max = j;
                }
            }
            copy3_lst1.add(i, max);
            copy3_lst1.remove(ind_max + 1);
        }
        System.out.println("Список 1 отсортированный пузырьковым методом по уменьшению:" + copy3_lst1);
    }

}
