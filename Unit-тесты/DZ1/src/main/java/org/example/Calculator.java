package org.example;

public class Calculator {

    /**
     * @param purchaseAmount сумма покупки
     * @param discountAmount размер скидки
     * @return возвращает сумму покупки с учетом скидки
     */
    public static double calculatingDiscount(double purchaseAmount, int discountAmount) {
        if (purchaseAmount<0){
            throw new ArithmeticException("Отрицательная сумма покупки");
        }
        if (purchaseAmount==0){
            throw new ArithmeticException("Сумма покупки равна 0");
        }
        if (discountAmount<0){
            throw new ArithmeticException("Размер скидки меньше 0");
        }

        double result = purchaseAmount - purchaseAmount*discountAmount/100;
        return result;
    }
}