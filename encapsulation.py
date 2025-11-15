#encapsulation
class rabbit:
  def __init__(self):
    self.public="anywhere"
    self.__private= "access via directly"
  def function(self):
    print(self.__private)
object = rabbit()
object.function()
