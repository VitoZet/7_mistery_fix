# Решатель квадратных уравнений

Это простой пример использования тестирования в Python.
* "quadratic_equation.py" является сценарием, который решает квадратичные уравнения и возвращает корни
* "tests.py" это тест для "quadratic_equation.py"

# Как использовать

* Склонируйте данный репозиторий
* Запустите файл tests.py

*Пример кода:*
```
import unittest

from quadratic_equation import get_roots


class QuadraticEquationTestCase(unittest.TestCase):
    def test_solves_real_roots(self):
        root1, root2 = get_roots(1, -2, 1)
        self.assertEqual(root1, 1)

    def test_first_root_less_than_second(self):
        root1, root2 = get_roots(1, 2, -3)
        self.assertEqual(root1, -3)
        self.assertEqual(root2, 1)

    def test_second_root_is_none_if_one_solution(self):
        root1, root2 = get_roots(1, -2, 1)
        self.assertIsNotNone(root1)
        self.assertIsNone(root2)

    def test_returns_none_for_complex_solution(self):
        root1, root2 = get_roots(1, 2, 3)
        self.assertIsNone(root1)
        self.assertIsNone(root2)
```

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
python tests.py # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
