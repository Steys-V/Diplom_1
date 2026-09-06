from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:

    # 1. Тест установки булочки
    def test_set_buns_sets_correct_bun(self):
        burger = Burger()
        mock_bun = Mock()

        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # 2. Тест добавления ингредиента
    def test_add_ingredient_adds_to_list(self):
        burger = Burger()
        mock_ingredient = Mock()

        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients
        assert len(burger.ingredients) == 1

    # 3. Тест удаления ингредиента по индексу
    def test_remove_ingredient_removes_from_list(self):
        burger = Burger()
        mock_ingredient = Mock()

        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert mock_ingredient not in burger.ingredients
        assert len(burger.ingredients) == 0

    # 4. Тест перемещения ингредиентов местами в списке
    def test_move_ingredient_changes_position(self):
        burger = Burger()
        mock_ing_1 = Mock()
        mock_ing_2 = Mock()

        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)

        # Перемещаем первый ингредиент на позицию второго
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ing_2
        assert burger.ingredients[1] == mock_ing_1

    # 5. Тест расчета стоимости (Используем моки с возвращаемыми значениями)
    def test_get_price_calculates_total_cost(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_price.return_value = 100.0  # Цена булки 100

        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 50.0  # Цена ингредиента 50

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        # Расчет: (100 * 2) + 50 = 250
        assert burger.get_price() == 250.0

    # 6. Тест печати чека (Мокаем методы булки и ингредиента для генерации текста)
    def test_get_receipt_returns_formatted_string(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = "Марсианская булка"
        mock_bun.get_price.return_value = 100.0

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "SAUCE"
        mock_ingredient.get_name.return_value = "Chili"
        mock_ingredient.get_price.return_value = 50.0

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        assert "(==== Марсианская булка ====)" in receipt
        assert "= sauce Chili =" in receipt
        assert "Price: 250.0" in receipt
