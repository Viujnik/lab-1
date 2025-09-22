from constants import OPERATIONS  # OPERATIONS: ключ(операция) - значение(выполнение операции для аргументов)


def check_it_int(a: float, b: float) -> bool:  # проверка чисел, что они целые
    return b % 1 == 0 and a % 1 == 0


def job_with_tokens(tokens: list) -> float:
    stack = []
    for token in tokens:  # перебор токенов для записи в стек и проведения операций
        if token in OPERATIONS:  # если токен - операция, достаем из стека 2 операнда и записываем в стек рез-тат операции
            try:
                b = stack.pop()
                a = stack.pop()
                if token in ['//', '%']:  # эти операция для целых чисел
                    if check_it_int(a, b):
                        result = OPERATIONS[token](a, b)
                        stack.append(result)
                    else:
                        print('Операция "//" разрешена только для целых чисел')
                        return
                else:
                    result = OPERATIONS[token](a, b)
                    stack.append(result)
            except IndexError:
                print("Ошибка: недостаточно операндов для оператора")
                return
            except ZeroDivisionError:
                print("Ошибка: деление на ноль")
                return
        else:  # операнды записываем в стек
            try:
                number = float(token)
                stack.append(number)
            except ValueError:
                print("Ошибка: неверный токен", token)
                return
    if len(stack) != 1:
        print("Ошибка: выражение содержит лишние операнды")
        return

    return stack[0]


def calculator(expression: str) -> float:
    tokens = expression.split()  # разбиваем выражение на токены
    return job_with_tokens(tokens)  # возвращаем результат обработки токенов


if __name__ == '__main__':
    print(calculator(input()))
