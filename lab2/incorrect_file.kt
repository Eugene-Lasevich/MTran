if ( x  = 10) {
    printf("x равен 10");
}
if (x  == 10&&true ) {
    printf("x равен 10");
}

var i1t: Int = 55
var tmp  = "sdfghj"

val 1number1:Double=123.45
val number2: Double = 6.022e23
val number3: Double = 1.234e-5

val number5: Double = 10e
val number6:Double =1-000.0
val number7: Double = 2.718м28e0




fun main() {
    var continueCalculation = true

    var переменная = 11



    while (continueCalculation) {
        println("Введите первое число:")
        val number1 = readLine()

        println("Введите второе число:")
        val number2 = readLine()

        println("Выберите операцию (+, -, *, /):")
        val operator = readLine()


        if (number1 == null || number2 == null || operator == null) {
            println("Ошибка: Неверный формат ввода чисел или операции")
            continue
        }

        val result = when (operator) {
            "+" -> number1 + number2
            "-" -> number1 - number2
            "*" -> number1 * number2
            "/" -> if (number2 != 0.0) number1 / number2 else "Ошибка: деление на ноль"
            else -> "Ошибка: неверная операция"
        }

        println("Результат: $result")

        println("Хотите продолжить? (да/нет)")
        val choice = readLine()

        continueCalculation = choice.equals("да", ignoreCase = true)
    }
    println("Спасибо за использование калькулятора!")
}
whi1e (i < 10) {
    println("Hello, World!")
}


if (x = 10) {
    printf("x равен 10");
}

message:String = "Привет, мир!"
