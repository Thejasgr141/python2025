class Game:
 def __init__(self, name, genre):
 self.name = name
 self.genre = genre

 def display(self):
 print(f"Game: {self.name}, Genre: {self.genre}, Created by Vinayak")
game1 = Game("BGMI", "Battle Royale")
game2 = Game("FIFA", "Sports")
game1.display()
game2.display()
