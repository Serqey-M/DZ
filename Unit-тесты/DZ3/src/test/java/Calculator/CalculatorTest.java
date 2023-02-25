package Calculator;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

class CalculatorTest {

    @Test
    void calculatingDiscountRegularDiscountAmount() {
        assertThat(Calculator.calculatingDiscount(2000.0, 50)).isEqualTo(1000); // обычная скидка
        assertThat(Calculator.calculatingDiscount(2000.0, 100)).isEqualTo(0); // обычная скидка
        assertThat(Calculator.calculatingDiscount(2000.0, 0)).isEqualTo(2000); // обычная скидка
    }

    @ParameterizedTest
    @ValueSource(ints = {110, -10})
    void calculatingDiscountInvalidDiscountAmount(int number) {
        assertThatThrownBy(() -> Calculator.calculatingDiscount(2000.0, number)).isInstanceOf(ArithmeticException.class)
                .hasMessage("Скидка должна быть в диапазоне от 0 до 100%"); // не допустимый процент скидки
    }

    @ParameterizedTest
    @ValueSource(ints = {110, -10, 50, 100, 0})
    void calculatingDiscountNegativePurchaseAmount(int number) {
        assertThatThrownBy(() -> Calculator.calculatingDiscount(-2000.0, number)).isInstanceOf(ArithmeticException.class)
                .hasMessage("Сумма покупки не может быть отрицательной"); // сумма покупки меньше 0
    }

    @Test
    void evenOddNumberEven() {
        assertTrue(Calculator.evenOddNumber(2));
    }

    @Test
    void evenOddNumberOdd() {
        assertFalse(Calculator.evenOddNumber(3));
    }

    @Test
    void numberInIntervalTrue() {
        assertTrue(Calculator.numberInInterval(30));
    }

    @ParameterizedTest
    @ValueSource(ints = {20, 25, 100, 120})
    void numberInIntervalFalse(int number) {
        assertFalse(Calculator.numberInInterval(number));
    }
}