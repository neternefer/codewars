#PPfTAB, chapter.8, Homework 4
#The Critter Caretaker Program
#Create critter's farm where you take care of all the critters.
#Each critter should have their attributes values assigned randomly.
import random
import sys
class Critter(object):
    farm = []
    moods = {}
    def __init__(self, name):
        self.boredom = random.randrange(0, 16)
        self.hunger = random.randrange(0, 16)
        self.name = name

    def talk(self):
        print("Hi, my name is", self.name, "and I'm", self.mood, "now.\n")
        self._pass_time()

    def eat(self, food = 4):
        print("Eating")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self._pass_time()

    def play(self, fun = 4):
        print("Playing")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self._pass_time()

    def __str__(self):
        p = "Your critters: \n"
        for n in Critter.moods.keys():
            p += (n + ", ")
        return p
    
    @property
    def mood(self):
        """Returns a string created on the fly"""
        moody = self.hunger + self.boredom
        if 5 > moody > 0:
            m = "Extatic"
            return m
        elif 10 > moody > 5:
            m = "Happy"
            return m
        elif 15 > moody > 5:
            m = "OK"
            return m
        elif 20 > moody > 15:
            m = "Unhappy"
            return m
        else:
            m = "Mad"
            return m

    def _pass_time(self):
        """Declared private as it should only be used by other methods"""
        self.boredom += 1
        self.hunger += 1

def main():
    animals_num = int(input("How many critters should your farm have?"))
    for i in range(animals_num):
        names = input("Enter name: ")
        c = Critter(names)
        Critter.farm.append(c)
        Critter.moods[c.name] = c.mood
    
    choice = None
    while choice != 0:
        choice = int(input("Enter number to select your option: "))
        print("""Options:
                 0 - exit
                 1 - talk
                 2 - eat
                 3 - play
              """)
        
        if choice == 0:
            print("Goodbye")
            sys.exit()
        elif choice == 1:
            for i in Critter.farm:
                i.talk()
        elif choice == 2:
            for i in Critter.farm:
                i.eat()
        elif choice == 3:
            for i in Critter.farm:
                i.play()
        else:
            print(c)


main()

            
    



    
