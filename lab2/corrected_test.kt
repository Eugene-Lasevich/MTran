

printf("x равен 10");
}
if (x == 10 && true) {
println("x равен 10");
}

var i1t : Int = 55
var tmp = "sdfghj"


val number2 : Double = 6.022e23
val number3 : Double = 1.234e5









fun main() {
var continueCalculation = true

var переменная = 11



while (continueCalculation) {
println("Введите первое число : ")
val number1 = readLine()

println("Введите второе число : ")
val number2 = readLine()

println("Выберите операцию ( + , - , * , / ) : ")
val operator = readLine()


if (number1 == null || number2 == null || operator == null) {
println("Ошибка : Неверный формат ввода чисел или операции")
continue
}

val result = when (operator) {
" + " -> number1 + number2
" - " -> number1 - number2
" * " -> number1 * number2
" / " -> if (number2 != 0.0) number1 / number2 else "Ошибка : деление на ноль"
else -> "Ошибка : неверная операция"
}

println("результат : $result")

println("Хотите продолжить? (да / нет)")
val choice = readLine()

continueCalculation = choice.equals("да", ignoreCase = true)
}
println("Спасибо за использование калькулятора ! ")
}

println("Hello, World ! ")
}





printf("x равен 10");
}
message : String = "Привет, мир ! "
