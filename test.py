import unittest
from main import remainder


class TestRemainder(unittest.TestCase):
    def test_remainder(self):
        test_cases = [
            (10, 3, 1),
            (25, 4, 1),
            (20, 5, 0),
            (-10, 3, 2),
            (10, -3, -2),
            (-10, -3, -1),
            (10, 0, "Деление на ноль невозможно.")  # Тест для деления на ноль
        ]

        for dividend, divisor, expected in test_cases:
            with self.subTest(dividend=dividend, divisor=divisor):
                if divisor == 0:
                    with self.assertRaises(ValueError) as context:
                        remainder(dividend, divisor)
                    self.assertEqual(str(context.exception), expected)
                    print(
                        f"Тест деления {dividend} на {divisor} прошел успешно: ожидаемое исключение. Сообщение: '{expected}'")
                else:
                    result = remainder(dividend, divisor)
                    self.assertEqual(result, expected)
                    print(f"Тест деления {dividend} на {divisor} прошел успешно: результат = {result}")

    def test_error_case(self):
        with self.assertRaises(ValueError):
            remainder(1, 0)  # Пример теста с ошибкой


if __name__ == '__main__':
    unittest.main()