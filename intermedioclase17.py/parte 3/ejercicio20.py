class Punto: 
  def __init__(self, x, y): 
    self._x = x
    self._y = y

  @property
  def x(self):
    return self._x

  @property
  def y(self):
    return self._y
  
punto = Punto(5, 10)
print(punto.x)  # 5
print(punto.y)  # 10
#punto.x = 10  # AttributeError: can't set AttributeError