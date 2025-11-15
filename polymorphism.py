#polymorphism
class belagavi:
  def tell(self):
    print("belagavi bedagi")
class tumkur(belagavi):
  def tell(self):
    print("not like")
obj=belagavi()
obj.tell()

obj1=tumkur()
obj1.tell()

