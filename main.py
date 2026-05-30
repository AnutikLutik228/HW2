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
