#Encapsulation 
class Thejas:
  def __init__(self):
   self.pub="ok"
   self._madhu="not ok"
  def Pavan_private(self):
   print(self._madhu)
kishore = Thejas()
print(kishore.pub)
kishore.Pavan_private()
