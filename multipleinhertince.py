class A:
 def feature1(self):
  print("Feature 1")
class B:
 def feature2(self):
  print("Feature 2")
class C(A, B):
   pass
obj = C()
obj.feature1()
