# AOfC_Day_01

import csv

class Game:
    def __init__(self, organisation, name, year):
        self.organization = organisation
        self.name = name
        self.year = year

    def __str__(self):
        return f"{self.organization}({self.name}))"

game_01 = Game("GDI", "AdventOfCode", 2023)

# print(game_01.organization, ': ', game_01.name, game_01.year)
# print(game_01)

#fileContent = open("EliseoAntonini\Data\input.txt", "r")
# print(fileContent.read())

#for data in fileContent:
#    print(data[3])

#fileContent.close()


with open('EliseoAntonini\Data\input_feed.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

