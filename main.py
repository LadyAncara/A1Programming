from boxdraw import drawbox


class Character:
    stats = [0, 0, 0, 0, 0]

    def __init__(self, name, arch, subarch, stats):
        self.name = name
        self.arch = arch
        self.subarch = subarch
        self.stats = stats


statnames = ['DEX', 'STR', 'AGI', 'WIS', 'INT']

Character.name = input("What is the name of your character? ")
Character.arch = input("What is your class? ")
Character.subarch = input("What is your subclass? ")
print("What are your following stats? ")

#TODO: make this not crash if the user doesnt put in numbers
for i in range(5):
    Character.stats[i] = int(input(f"What is your {statnames[i]}? "))

#gets the proficiency bonus from entred stat values
statbonus = list(map(lambda x: int(x), list(map(lambda x: ((x - (x % 2)) / 2) - 5, Character.stats))))

#uses drawbox() to format out haracter sheet to be nice and pretty
prev = drawbox('TOP', [], 42 + len(Character.name), 1, f"Name: {Character.name}", 30 + len(Character.name), "Level: 1")
drawbox('BOTTOM', prev, 42 + len(Character.name), 1, f"Class: {Character.arch}", 12 + len(Character.arch),
        f"Archetype: {Character.subarch}")

prev = drawbox('TOP', [], 42, 1, "STAT", 14, "POINTS", 28, "PROF")
for i in range(len(Character.stats) - 1):
    drawbox('MIDDLE', prev, 42, 1, statnames[i], 14, str(Character.stats[i]), 28, str(statbonus[i]))
drawbox('BOTTOM', prev, 42, 1, statnames[4], 14, str(Character.stats[4]), 28, str(statbonus[4]))
