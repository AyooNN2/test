from player import Player

class Warrior(Player):

    def __init__(self, pseudo, health, attack):
        super().__init__(pseudo,health,attack)
        self.armor = 3
        print("Bienvenue au guerrier", pseudo, "/ Points de vie: ", health, "/ Attaque", attack, "/ Armure", self.armor)


    def damage(self, damage):
        if self.armor > 0:
            self.armor -= 1
            damage = 0
            super().damage(damage)

    def blade(self):
        self.armor = 3
        print("Les points d'armure ont été rechargées")

    def get_armor_value(self):
        return self.armor

                
player1 = Player("AyooN",100,25)
warrior1 = Warrior("DarkWarrior",125,4)
if issubclass(Warrior, Player):
    print("CACA")