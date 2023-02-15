//1) Нужно написать в калькуляторе метод вычисления суммы покупки (метод принимает сумму, процент скидки и возвращает сумму со скидкой) и проверить его используя AssertJ
// (отрицательное числа, 0, проценты>=100% , процент< 0%, обычные скидки). Все ошибки должны быть обработаны, при вводе недопустимых аргументов можно выбрасывать
// (throw new ArithmeticException("Суть ошибки");), но нужно проверить, что все ошибки проверяются в тестах.
package org.example;

import static org.assertj.core.api.Assertions.*;

public class CalculatorTest {
    public static void main(String[] args) {
        assertThatThrownBy(() -> Calculator.calculatingDiscount(-10, 3)).isInstanceOf(ArithmeticException.class);
        assertThatThrownBy(() -> Calculator.calculatingDiscount(0, 3)).isInstanceOf(ArithmeticException.class);
        assertThat(Calculator.calculatingDiscount(100, 3)).isEqualTo(97);
        assertThat(Calculator.calculatingDiscount(100, 100)).isEqualTo(0);
        assertThat(Calculator.calculatingDiscount(100, 0)).isEqualTo(100);
        assertThatThrownBy(() -> Calculator.calculatingDiscount(100, -10)).isInstanceOf(ArithmeticException.class);
        assertThatThrownBy(() -> Calculator.calculatingDiscount(-100, -10)).isInstanceOf(ArithmeticException.class);
        assertThatThrownBy(() -> Calculator.calculatingDiscount(0, 0)).isInstanceOf(ArithmeticException.class);
    }
}