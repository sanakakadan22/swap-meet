class Item:
  def __init__(self, category="", condition=0):
    self.category = category
    self.condition = condition

  def condition_description(self):
    if self.condition < 1:
      return "You probably want a glove for this one..."
    elif self.condition < 2:
      return "Hope you aren't counting on this working for very long"
    elif self.condition < 3:
      return "It may not be pretty but its sturdy!"
    elif self.condition < 4:
      return "It's been used but still great!"
    elif self.condition < 5:
      return "Almost like its brand new!"
    else:
      return "Never been opened!"

  def __str__(self):
    return "Hello World!"