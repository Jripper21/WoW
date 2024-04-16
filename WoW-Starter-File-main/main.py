# Import classes from team members
from character import Character
from enemy import Enemy
from item import Item
from environment import Environment

def main():
    # Game initialization code goes here
    hero = Character("Arthas", 30, 100)
    villain = Enemy("Mal'Ganis", 25, 80)
    sword = Item("Excalibur", "Sword", 20)
    forest = Environment("Elwynn Forest")

    # Example of interactions
    print(hero)
    print(villain)
    hero.attack()
    villain.take_damage(hero.attack())
    print(forest)

if __name__ == "__main__":
    main()
