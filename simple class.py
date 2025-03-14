class V:
 def __init__(self, brand, size):
 self.brand = brand
 self.size = size

 def display(self):
 print(f"TV Brand: {self.brand}, Size: {self.size} inches, Created by Vinayak")
tv = TV("Samsung", 55)
tv.display()
