def check_it_int(a: float, b: float) -> bool:  # проверка чисел, что они целые
    return b % 1 == 0 and a % 1 == 0


def job_with_tokens(tokens: list) -> float:
    stack = []
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '**': lambda a, b: a ** b,
        '//': lambda a, b: a // b,
        '%': lambda a, b: a % b

    }
    for token in tokens:  # перебор токенов для записи в стек и проведения операций
        if token in operations:  # если токен - операция, достаем из стека 2 операнда и записываем в стек рез-тат операции
            try:
                b = stack.pop()
                a = stack.pop()
                if token in ['//', '%']:  # эти операция для целых чисел
                    if check_it_int(a, b):
                        result = operations[token](a, b)
                        stack.append(result)
                    else:
                        print(f'Операция "{token}" разрешена только для целых чисел')
                        return
                else:
                    result = operations[token](a, b)
                    stack.append(result)
            except IndexError:
                print("Ошибка: недостаточно операндов для оператора")
                return
            except ZeroDivisionError:
                print("Ошибка: деление на ноль")
                return
            except OverflowError:
                print("Результатом является слишком длянное число")
                return
        else:  # операнды записываем в стек
            try:
                number = float(token)
                stack.append(number)
            except ValueError:
                print("Ошибка: неверный токен: ", token)
                return
    if len(stack) != 1:
        print("Ошибка: выражение содержит лишние операнды")
        return

    return stack[0]


def calculator(expression: str) -> float:
    if expression == '':
        print("Введите непустую строку")
        return "Была найдена ошибка."
    tokens = expression.replace('(', '').replace(')', '').split()  # разбиваем выражение на токены, игнорирую скобки
    res_of_calc = job_with_tokens(tokens)
    if res_of_calc != None:
        return res_of_calc
    return "Была найдена ошибка."


if __name__ == '__main__':
    print(calculator(input()))
