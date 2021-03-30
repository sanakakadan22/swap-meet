class Vendor:
  def __init__(self, inventory=[]) -> None:
    self.inventory = inventory

  def add(self, item):
    self.inventory.append(item)
    return item

  def remove(self, item):
    matched = False
    for candidate in self.inventory:
      if item == candidate:
        self.inventory.remove(candidate)
        matched = candidate
    return matched

  def get_by_category(self, category):
    def matches_category(item):
      return item.category == category
    return list(filter(matches_category, self.inventory))

  def swap_items(self, other, my_item, their_item):
    if len(self.inventory) < 1 or len(other.inventory) < 1:
      return False
    try:
      self.inventory.remove(my_item)
      other.inventory.remove(their_item)
    except ValueError:
      return False
    self.inventory.append(their_item)
    other.inventory.append(my_item)
    return True

  def swap_first_item(self, other):
    return self.swap_items(other, self.inventory[0], other.inventory[0])

  def get_best_by_category(self, category):
    items_in_category = self.get_by_category(category)
    def get_condition(item):
      return item.condition
    return max(items_in_category, key = get_condition) if len(items_in_category) > 0 else None

  def swap_best_by_category(self, other, my_priority, their_priority):
    my_best = self.get_best_by_category(their_priority)
    their_best = other.get_best_by_category(my_priority)
    return self.swap_items(other, my_best, their_best)

