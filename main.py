class Ingredient:
  def __init__(self, name: str, quantity: float, unit: str):
    self.name = name
    self.quantity = quantity
    self.unit = unit

  @property
  def quantity(self):
    return self._quantity

  @quantity.setter
  def quantity(self, value):
    value = float(value)
    if value <= 0:
      raise ValueError("Количество должно быть положительным")

    self._quantity = value

    def __str__(self):
      return (f"{self.name}: {self.quantity}{self.unit}")

    def __repr__(self):
      return (f"Ingridient('{self.name}', {self.quantity}, '{self.unit}')")

    def __eq__(self, other):
      return self.name == other.name and self.unit == other.unit

class Recipe:
  def __init__(self, title, ingredients):
    self.title = title
    self.ingredients = ingredients

  def add_ingredient(self, ingredient):
    for i in self.ingredients:
      if i == ingredient:
        i.quantity = i.quantity + ingredient.quantity
        return
    self.ingredients.append(ingredient)

  @staticmethod
  def is_valid_ratio(ratio):
    if type(ratio) == int or type(ratio) == float:
      if ratio > 0:
        return True

    return False

  def scale(self, ratio):
    new_ingredients = []
    for ingredient in self.ingredients:
      new_ingredient = Ingredient(ingredient.name, ingredient.quantity * ratio, ingredient.unit)

      new_ingredients.append(new_ingredient)

    new_recipe = Recipe(self.title, new_ingredients)
    return new_recipe

  def __len__(self):
    return len(self.ingredients)

  def __str__(self):
    result = self.title + "\n"

    for ingredient in self.ingredients:
      result = result + str(ingredient) + "\n"
    return result

class ShoppingList:
  def __init__(self):
    self._items = []

  def add_recipe(self, recipe, portions):
    if portions <= 0:
      raise ValueError("Количество порций должно быть положительным")

    scaled_recipe = recipe.scale(portions)

    for ingredient in scaled_recipe.ingredients:
      self._items.append((ingredient, recipe.title))

  def remove_recipe(self, title):
    new_items = []

    for item in self._items:
      if item[1] != title:
        new_items.append(item)

    self._items = new_items

  def get_list(self):
    products = {}

    for item in self._items:
      ingredient = item[0]

      key = (ingredient.name, ingredient.unit)

      if key in products:
        products[key] += ingredient.quantity
      else:
        products[key] = ingredient.quantity

    result = []

    for key in products:
      name = key[0]
      unit = key[1]
      quantity = products[key]

      result.append(Ingredient(name, quantity, unit))

    result.sort(key=lambda x: x.name)

    return result

  def __add__(self, other):
    new_shopping_list = ShoppingList()

    for item in self._items:
      new_shopping_list._items.append(item)

    for item in other._items:
      new_shopping_list._items.append(item)

    return new_shopping_list


class DietaryRecipe(Recipe):
  def __init__(self, title, diet_type, ingredients):
    super().__init__(title, ingredients)
    self.diet_type = diet_type

  def scale(self, ratio):
    new_recipe = super().scale(ratio)

    return DietaryRecipe(new_recipe.title, self.diet_type, new_recipe.ingredients)

  def __str__(self):
    return f"[{self.diet_type}] {self.title}"
