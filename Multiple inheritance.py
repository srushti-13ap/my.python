#multiple inheritance
class A:
  def fun1(self):
    print("the best")
class B:
  def fun2(self):
    print("better")
class C:
  def fun3(self):
    print("good")

obj1=A()
obj1.fun1()

obj2=B()
obj2.fun2()

obj3=C()
obj3.fun3()
