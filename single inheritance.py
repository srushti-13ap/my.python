#single inheritance
class parent:
  def function(self):
    print("good girl")
class child(parent):
  def function(self):
    print("bad girl")
obj=parent()
obj.function()

obj1=child()
obj1.function()
