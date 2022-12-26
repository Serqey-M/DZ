const tempCelsius = +prompt('Введите температуру в градусах Цельсия');
const tempFahrenheit = Math.floor(((9 / 5) * tempCelsius + 32) * 100) / 100;
alert(`Цельсий: ${tempCelsius}, Фаренгейт: ${tempFahrenheit}`);