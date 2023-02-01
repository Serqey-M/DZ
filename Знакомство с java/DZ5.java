import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Set;

// 1. Создать словарь HashMap. Обобщение <Integer, String>.
// 2. Заполнить пятью ключами (индекс, ФИО+Возраст+Пол "Иванов Иван Иванович 28 м"), добавить ключь, если не было!)
// 3. Изменить значения сделав пол большой буквой.
// 4. Пройти по коллекции и вывести значения в формате Фамилия инициалы "Иванов И.И."
// 5. *Сортировать значения по возрасту и вывести отсортированную коллекция как в четвёртом пункте.
public class DZ5 {
    public static void main(String[] args) {
        // 1
        HashMap<Integer, String> hashMap = new HashMap<>();
        // 2
        System.out.println("Задание 2");
        hashMap.putIfAbsent(1, "Иванов Иван Иванович 25 м");
        hashMap.putIfAbsent(2, "Петров Петр Петрович 30 м");
        hashMap.putIfAbsent(3, "Сидоров Сидор Сидорович 18 м");
        hashMap.putIfAbsent(4, "Иванова Иванна Ивановна 35 ж");
        hashMap.putIfAbsent(5, "Петрова Петра Петровна 20 ж");
        hashMap.putIfAbsent(5, "Сидорова Сидора Сидоровна 35 ж");
        System.out.println(hashMap + "\r\n");
        // 3
        System.out.println("Задание 3");
        Set<Integer> keySet = hashMap.keySet();
        for (int i = 0; i < keySet.size(); i++) {
            if (hashMap.get(keySet.toArray()[i]).charAt(hashMap.get(keySet.toArray()[i]).length() - 1) == "м"
                    .charAt(0)) {
                hashMap.compute((Integer) keySet.toArray()[i], (k, v) -> v = v.replaceFirst(".$", "М"));
            } else if ((hashMap.get(keySet.toArray()[i]).charAt(hashMap.get(keySet.toArray()[i]).length() - 1) == "ж"
                    .charAt(0))) {
                hashMap.compute((Integer) keySet.toArray()[i], (k, v) -> v = v.replaceFirst(".$", "Ж"));
            }
        }
        System.out.println(hashMap + "\r\n");
        // 4
        System.out.println("Задание 4");
        for (int i = 0; i < keySet.size(); i++) {
            System.out.println(hashMap.get(keySet.toArray()[i]).split(" ")[0] + " "
                    + hashMap.get(keySet.toArray()[i]).split(" ")[1].charAt(0) + "."
                    + hashMap.get(keySet.toArray()[i]).split(" ")[2].charAt(0) + ".");
        }
        System.out.println();
        // 5
        System.out.println("Задание 5");
        LinkedList<Integer> age = new LinkedList<>();
        LinkedList<Integer> index = new LinkedList<>();
        ArrayList<String> fio =new ArrayList<>();
        for (int i = 0; i < keySet.size(); i++) {
            age.add(Integer.valueOf(hashMap.get(keySet.toArray()[i]).split(" ")[3]));
            index.add(i);
            fio.add(hashMap.get(keySet.toArray()[i]).split(" ")[0] + " "
            + hashMap.get(keySet.toArray()[i]).split(" ")[1].charAt(0) + "."
            + hashMap.get(keySet.toArray()[i]).split(" ")[2].charAt(0) + ".");
        }
        for (int i = 0; i < age.size(); i++) {
            int max = age.get(i);
            int ind_max = i;
            for (int j = i + 1; j < age.size(); j++) {
                if (max <age.get(j)) {
                    max = age.get(j);
                    ind_max = j;
                }
            }
            age.add(i, age.get(ind_max));
            age.remove(ind_max + 1);
            index.add(i, index.get(ind_max));
            index.remove(ind_max + 1);
        }
        for (int i = 0; i < index.size(); i++) {
            System.out.println(fio.get(index.get(i)));
        }
    }
}
