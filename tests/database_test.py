from praktikum.database import Database

class TestDatabase:

    # 1.  тест: проверка точного количества булочек в базе данных
    def test_available_buns_returns_correct_count(self):
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3

    # 2.  тест: проверка содержимого списка булочек (названия)
    def test_available_buns_contains_correct_names(self):
        database = Database()
        buns = database.available_buns()
        assert buns[0].get_name() == "black bun"
        assert buns[1].get_name() == "white bun"
        assert buns[2].get_name() == "red bun"

    # 3.  тест: проверка точного количества ингредиентов в базе данных
    def test_available_ingredients_returns_correct_count(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6

    # 4.  тест: проверка точечного содержимого списка ингредиентов
    def test_available_ingredients_contains_correct_names(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[-1].get_name() == "sausage"
