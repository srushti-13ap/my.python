def userdetails(x,y):
  name = input("enter your name: ")
  age = int(input("enter your age: "))
  rollno = int(input("enter your roll no: "))
  add = age+rollno
  print("the sum is: ",add)
  mul =  age*rollno
  print("the mul is: ",mul)
  return name,age,rollno
userdetails(5,9) #you give any number in x,y
