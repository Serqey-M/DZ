package simple_shopping_cart;

import model.Cart;
import model.Shop;
import org.junit.jupiter.api.Test;
import model.Product;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

import java.io.ByteArrayOutputStream;
import java.util.ArrayList;
import java.util.List;

import static org.assertj.core.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

class ShopTest {

    /**
     * Создаем набор продуктов для магазина:
     *
     * @return список продуктов
     */
    public static List<Product> getStoreItems() {
        List<Product> products = new ArrayList<>();

        // Три массива Названия, Цены, Кол-во
        String[] productNames = {"bacon", "beef", "ham", "salmon", "carrot", "potato", "onion", "apple", "melon", "rice", "eggs", "yogurt"};
        Double[] productPrice = {170.00d, 250.00d, 200.00d, 150.00d, 15.00d, 30.00d, 20.00d, 59.00d, 88.00d, 100.00d, 80.00d, 55.00d};
        Integer[] stock = {10, 10, 10, 10, 10, 10, 10, 70, 13, 30, 40, 60};

        // Последовательно наполняем список продуктами
        for (int i = 0; i < productNames.length; i++) {
            products.add(new Product(i + 1, productNames[i], productPrice[i], stock[i]));
        }
        return products;
    }

    private ByteArrayOutputStream output = new ByteArrayOutputStream();


/*
            ID | Название  | Цена, р. | Кол-во в магазине, шт.
            1  | bacon     | 170.0    | 10
            2  | beef      | 250.0    | 10
            3  | ham       | 200.0    | 10
            4  | salmon    | 150.0    | 10
            5  | carrot    | 15.0     | 10
            6  | potato    | 30.0     | 10
            7  | onion     | 20.0     | 10
            8  | apple     | 59.0     | 70
            9  | melon     | 88.0     | 13
            10 | rice      | 100.0    | 30
            11 | eggs      | 80.0     | 40
            12 | yogurt    | 55.0     | 60
*/

    /**
     * 2.7. Нужно написать юнит-тест для проверки следующей <b>ситуации</b>:
     * Пользователь вводит неверный номер продукта
     * <br><b>Ожидаемый результат:</b>
     * Исключение типа RuntimeException и сообщение Не найден продукт с id
     * *Сделать тест параметризованным
     */
    @Test
    void incorrectProductSelectionCausesException() {
        // Arrange (Подготовка)
        Shop shop = new Shop(getStoreItems());
        Cart cart = new Cart(shop);
        // Act (Выполнение)

        // Assert (Проверка утверждения)
        assertThatThrownBy(() -> cart.addProductToCartByID(13)).isInstanceOf(RuntimeException.class).hasMessage("Не найден продукт с id: 13");;
    }
    @ParameterizedTest
    @ValueSource(ints = {-1, 0, 13})
    void incorrectProductSelectionCausesException1(int number) {
        // Arrange (Подготовка)
        Shop shop = new Shop(getStoreItems());
        Cart cart = new Cart(shop);
        // Act (Выполнение)

        // Assert (Проверка утверждения)
        assertThatThrownBy(() -> cart.addProductToCartByID(number)).isInstanceOf(RuntimeException.class).hasMessage("Не найден продукт с id: %s", number);;
    }
    }