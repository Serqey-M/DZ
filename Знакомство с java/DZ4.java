import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;

// 1.Сохранить в файл строку и загрузить из файла строку с выводом в консоль используя классы FileWriter и FileReader
// 2.Загрузить из файла многострочный текст формата ФИО возраст и пол через пробелы. Разбить по строкам и вывести в консоль в формате "Иванов И.И. 32 М"
// 3.Загруженный и разбитый по строкам текст загрузить в подготовленные списки. Фамилии, имена, отчества, возрас и пол в отдельных списках.
// 4.Отсортировать по возрасту используя дополнительный список индексов.

public class DZ4 {
    public static void main(String[] args) {
        // 1.
        try {
            FileWriter writer = new FileWriter("Hello.text");
            writer.append("Привет мир");
            writer.flush();
            writer.close();
            String str = "";
            FileReader reader = new FileReader("Hello.text");
            while (reader.ready()) {
                str += (char) reader.read();
            }
            System.out.println("Задание 1: " + str);
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        // 2.
        try {
            String str = "";
            FileReader reader = new FileReader("bd.sgl");
            while (reader.ready()) {
                str += (char) reader.read();
            }
            reader.close();
            String[] array = str.split("\n");
            System.out.println("Задание 2:");
            for (int i = 0; i < array.length; i++) {
                String[] arrayi = array[i].split(" ");
                System.out.println(arrayi[0] + " " + arrayi[1].substring(0, 1) + ". " + arrayi[2].substring(0, 1) + ". "
                        + arrayi[3] + " " + arrayi[4]);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        // 3.
        ArrayList<String> family = new ArrayList<>();
        ArrayList<String> name = new ArrayList<>();
        ArrayList<String> soname = new ArrayList<>();
        ArrayList<Integer> age = new ArrayList<>();
        ArrayList<String> gender = new ArrayList<>();
        LinkedList<Integer> index = new LinkedList<>();
        try {
            String str = "";
            FileReader reader = new FileReader("bd.sgl");
            while (reader.ready()) {
                str += (char) reader.read();
            }
            reader.close();
            String[] array = str.split("\r\n");
            System.out.println("Задание 3:");
            for (int i = 0; i < array.length; i++) {
                String[] arrayi = array[i].split(" ");
                family.add(arrayi[0]);
                name.add(arrayi[1]);
                soname.add(arrayi[2]);
                age.add(Integer.valueOf(arrayi[3]));
                gender.add(arrayi[4]);
                index.add(i);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println(family);
        System.out.println(name);
        System.out.println(soname);
        System.out.println(age);
        System.out.println(gender);
        // 4.
        System.out.println("Задание 4:");
        LinkedList<Integer> copi_age = new LinkedList<>(age);
        for (int i = 0; i < copi_age.size(); i++) {
            int max = copi_age.get(i);
            int ind_max = i;
            for (int j = i + 1; j < copi_age.size(); j++) {
                if (max < copi_age.get(j)) {
                    max = copi_age.get(j);
                    ind_max = j;
                }
            }
            copi_age.add(i, copi_age.get(ind_max));
            copi_age.remove(ind_max + 1);
            index.add(i, index.get(ind_max));
            index.remove(ind_max + 1);
        }
        for (int i = 0; i < index.size(); i++) {

            System.out.print(family.get(index.get(i)) + " ");
            System.out.print(name.get(index.get(i)) + " ");
            System.out.print(soname.get(index.get(i)) + " ");
            System.out.print(age.get(index.get(i)) + " ");
            System.out.printf(gender.get(index.get(i)) + " ");
            System.out.println();
        }
    }
}