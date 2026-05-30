import pytest
from main import *

def test_create_ingredient():
    i = Ingredient("Мука", 500, "г")
    assert i.name == "Мука"
    assert i.quantity == 500.0
    assert i.unit == "г"

def test_str():
    i = Ingredient("Мука", 500, "г")
    assert str(i) == "Мука: 500.0г"

def test_eq_same():
    i1 = Ingredient("Мука", 500, "г")
    i2 = Ingredient("Мука", 1000, "г")
    assert i1 == i2

def test_eq_different_name():
    i1 = Ingredient("Мука", 500, "г")
    i2 = Ingredient("Сахар", 500, "г")
    assert i1 != i2

def test_eq_different_unit():
    i1 = Ingredient("Мука", 500, "г")
    i2 = Ingredient("Мука", 500, "кг")
    assert i1 != i2



def test_create_recipe():
    ingredients = [Ingredient("Авокадо", 2, "шт")]
    recipe = Recipe("Тост", ingredients)
    assert recipe.title == "Тост"
    assert recipe.ingredients == ingredients

def test_add_new_ingredient():
    recipe = Recipe("Смузи", [])
    recipe.add_ingredient(Ingredient("Манго", 1, "шт"))
    assert len(recipe.ingredients) == 1

def test_add_same_ingredient():
    recipe = Recipe("Смузи", [])
    recipe.add_ingredient(Ingredient("Манго", 1, "шт"))
    recipe.add_ingredient(Ingredient("Манго", 2, "шт"))
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].quantity == 3.0

def test_scale_creates_new_recipe():
    recipe = Recipe("Коктейль", [Ingredient("Киви", 2, "шт")])
    new_recipe = recipe.scale(2)
    assert recipe is not new_recipe

def test_scale_multiplies_quantity():
    recipe = Recipe("Коктейль", [Ingredient("Киви", 2, "шт")])
    new_recipe = recipe.scale(3)
    assert new_recipe.ingredients[0].quantity == 6.0

def test_scale_invalid_ratio():
    recipe = Recipe("Коктейль", [Ingredient("Киви", 2, "шт")])
    with pytest.raises(ValueError):
        recipe.scale(0)

def test_len():
    recipe = Recipe("Завтрак",[Ingredient("Авокадо", 1, "шт"), Ingredient("Лосось", 100, "г")])
    assert len(recipe) == 2

def test_add_recipe():
    r = Recipe("Боул", [Ingredient("Нут", 100, "г")])
    s = ShoppingList()
    s.add_recipe(r, 2)
    result = s.get_list()
    assert len(result) == 1
    assert result[0].name == "Нут"
    assert result[0].quantity == 200.0

def test_add_recipe_bad_portions():
    r = Recipe("Боул", [Ingredient("Нут", 100, "г")])
    s = ShoppingList()
    with pytest.raises(ValueError):
        s.add_recipe(r, 0)

def test_remove_recipe():
    r1 = Recipe("Боул", [Ingredient("Нут", 100, "г")])
    r2 = Recipe("Салат", [Ingredient("Руккола", 50, "г")])
    s = ShoppingList()
    s.add_recipe(r1, 1)
    s.add_recipe(r2, 1)
    s.remove_recipe("Боул")
    result = s.get_list()
    assert len(result) == 1
    assert result[0].name == "Руккола"

def test_remove_not_existing_recipe():
    r = Recipe("Боул", [Ingredient("Нут", 100, "г")])
    s = ShoppingList()
    s.add_recipe(r, 1)
    s.remove_recipe("Суп из облаков")
    assert len(s.get_list()) == 1

def test_get_list_sums_same_ingredients():
    r1 = Recipe("Боул", [Ingredient("Нут", 100, "г")])
    r2 = Recipe("Суп", [Ingredient("Нут", 50, "г")])
    s = ShoppingList()
    s.add_recipe(r1, 1)
    s.add_recipe(r2, 1)
    result = s.get_list()
    assert len(result) == 1
    assert result[0].quantity == 150.0

def test_get_list_sorted():
    r = Recipe("Странный салат", [Ingredient("Яблоко", 1, "шт"), Ingredient("Авокадо", 1, "шт")])
    s = ShoppingList()
    s.add_recipe(r, 1)
    result = s.get_list()
    assert result[0].name == "Авокадо"
    assert result[1].name == "Яблоко"

def test_add_shopping_lists():
    r1 = Recipe("Боул", [Ingredient("Нут", 100, "г")])
    r2 = Recipe("Салат", [Ingredient("Руккола", 50, "г")])
    s1 = ShoppingList()
    s2 = ShoppingList()
    s1.add_recipe(r1, 1)
    s2.add_recipe(r2, 1)
    s3 = s1 + s2
    assert len(s3.get_list()) == 2
    assert len(s1.get_list()) == 1
    assert len(s2.get_list()) == 1




