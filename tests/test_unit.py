from src.main import calculator


# проверка простейших выражений
def test_simpl_expression():
    res = [calculator('6 6 +'), calculator('6 5.5 -'), calculator('6 6 *'), calculator('6 6 /'), calculator('7 2 //'),
           calculator('6 3 **'), calculator('12 8 %')]
    assert res == [12.0, 0.5, 36.0, 1.0, 3.0, 216.0, 4.0]


# проверка на выражения с ошибками
def test_error_expression():
    res = [calculator('9 0 /'), calculator(' 12.5 9 //'), calculator('45 % 11.4'), calculator(''),
           calculator('12 3 - +'), calculator('34 888 **')]
    assert res == ['Была найдена ошибка.'] * 6


# проверка более сложных выражений(и сюда же скобки и лишние пробелы)
def test_hard_expression():
    res = [calculator('45 6 % 123 10 // + 10.5 *'), calculator('( ( 6 12 * )    5 3 **  + 100 - 13 %'),
           calculator('12 1 + 6 * 6 **')]
    assert res == [157.5, 6.0, 225199600704.0]
