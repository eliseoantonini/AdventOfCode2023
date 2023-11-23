# AOfC_Day_01

class Game:
    def __init__(self, organisation, name, year):
        self.organization = organisation
        self.name = name
        self.year = year

    def __str__(self):
        return f"{self.organization}({self.name}))"

game_01 = Game("GDI", "AdventOfCode", 2023)

print(game_01.organization, ': ', game_01.name, game_01.year)

print(game_01)

fileContent = open("Data\input.txt", "r")
print(fileContent.read())

