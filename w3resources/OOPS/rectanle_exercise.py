class Rectangle:
  def __init__(self, l, w):
    self.length = l
    self.width = w
    
  def area(self):
    return self.length*self.width
  
newRectangle = Rectangle(4,5)
print(newRectangle.area())