# object oriented programming
class areaofcircle:
  def __init__(self,pi,radius):
    self.pi=pi
    self.radius=radius
  def circle(self):
      return self.pi*self.radius*self.radius
circle2 = areaofcircle(3.14,10)
circle2.circle()
