
// Разработать программу, имитирующую поведение коллекции HashSet. В программе содать метод add добавляющий элемент, и метод позволяющий выводить эллементы коллекции в консоль. Формат данных Integer.
import java.util.HashMap;

public class DZ6 {
    public static HashMap<Integer, Object> hashMap = new HashMap<>();
    private static final Object OBJECT = new Object();

    public static void main(String[] args) {
        add(65);
        add(5);
        add(45);
        System.out.println(hashMap.keySet());
        getString();
        getString2();
        getKey(1);
    }

    public static void add(Integer number) {
        hashMap.put(number, OBJECT);
    }

    public static void getString() {
        System.out.println(hashMap.keySet());
    }

    public static void getString2() {
        Object[] tmp = hashMap.keySet().toArray();
        for (Object object : tmp) {
            System.out.println(object);
        }
    }

    public static void getKey(int index) {
        try {
            System.out.println(hashMap.keySet().toArray()[index]);
        } catch (Exception e) {
            System.out.println("ключа с данным индексом не существует");
        }
    }
}