#Using the code from the character file to make the enemy
from character import Character

class Enemy(Character):
    def __init__(self, name, health, durability, attack_damage):
        super().__init__(name, health, durability) #Makes the code more organized and not as big
        self.__attack_damage = attack_damage
        self.__damage_num = 4
        
#The enemy's attack strategy
    def att_strategy(self):
        if self.__damage_num > 8:
            return "uses a killer attack!"
        else:
            return "uses a normal attack!"
        
    def attack(self):
        attack_type = self.plan_attack()
        return f"{self.__str__()} {attack_type}"

    def __str__(self):
        info = super().__str__()
        print(f"{info}\nAttack Damage: {self.__attack_damage}\nDamage: {self.__damage_num}")
        
#In use since there is a name for the enemy
if __name__ == "__main__":
    generic_enemy = Enemy("Skeleton", 17, 5, 6)
    print(generic_enemy.attack())
