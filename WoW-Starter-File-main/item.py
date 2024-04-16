class Item:
    def __init__(self, name, item_type, power):
        self.__name = name  # private attribute
        self.__type = item_type  # private attribute
        self.__power = power  # private attribute

    def use(self, character):
        if self.__name == "Excalibur":
            print(f"{character._Character__name} used {self.__name}. It's a powerful sword!")
            character._Character__strength += self.__power  # Increase character's strength by the power of Excalibur
            print(f"{character._Character__name}'s strength increased by {self.__power}.")
        else:
            print(f"There's no effect. {character._Character__name} cannot use {self.__name}.")

    def __str__(self):
        return f"{self.__name} ({self.__type}), Power: {self.__power}"
