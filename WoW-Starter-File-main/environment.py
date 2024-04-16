 class Environment:
    def __init__(self, name, description):
        self.__name = name  # Private attribute
        self.__description = description

    def view(self):
        print(f"The place you are currently in is named {self.__name}.  {self.__description}")

