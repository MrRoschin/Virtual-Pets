class Pet():
    def __init__(self, name, age, hunger, boredom, sleepiness, dead):
        self.dead = False
        self.name = name
        self.age = age
        self.hunger = hunger
        self.boredom = boredom
        self.sleepiness = sleepiness
        self._Pet__dead = False

    def __str__(self):
        string = f"""Name: {self.name}
Age: {self.age}
Hunger: {self.hunger}
Boredom: {self.boredom}
Sleepiness: {self.sleepiness}
Dead? {self.dead}
"""
        return string

    def feed(self):
        self.hunger -= 3
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} has been fed.\nUpdated Hunger: {self.hunger}")

    def play(self):
        self.boredom -= 3
        if self.boredom < 0:
            self.boredom = 9
        print(f"{self.name} has been entertained.\nUpdated Boredom: {self.boredom}")

    def sleep(self):
        self.sleepiness -= 5
        if self.sleepiness < 0:
            self.sleepiness = 9
        print(f"{self.name} has slept.\nUpdated Sleepiness: {self.sleepiness}")

    def wait(self):
        if self._Pet__dead:
            print(f"{self.name} is dead and cannot wait.")
            return
        self.age += 1
        self.hunger += 1
        self.boredom += 1
        self.sleepiness += 1
        print(f"{self.name} has aged a year.\nUpdated Age: {self.age}\nUpdated Hunger: {self.hunger}\nUpdated Boredom: {self.boredom}\nUpdated Sleepiness: {self.sleepiness}")
        self.check_death()

####----Task 1----####
#Set up your pet with the following attributes:
#name (make this mandatory), age (default:0), hunger (default: 5), boredom (default:3), sleepiness(default:3)

age = 0; hunger = 5; boredom = 3; sleepiness = 3; dead = 0

####----Task 2----####
#instantiate your pet object with the name of your choice

petname = input("Enter the name of your pet: ")

pet1 = Pet(petname, age, hunger, boredom, sleepiness, dead)
print(pet1)
# Here just in case: print(f"{pet1}'s stats\n-------------\nStatus: {'Dead' if dead else 'Alive'}\n\nAge: {age}\nHunger: {hunger}\nBoredom: {boredom}\nSleepiness: {sleepiness}")

####----Task 3----#### 
# We need to add the following methods to our Virtual Pet:
# 1. Feed - which will reduce hunger by 3
# use a selection to make sure if hunger goes below zero it gets reset to 0 (we don’t want any negative numbers.)
# 2. Play - which will reduce boredom by 3
# 3. Sleep - which will reduce sleepiness by 5
# 4. Wait - which will increase age, and increase hunger, boredom and sleepiness
# 5. Is_dead - which will check to see if the Pet has hit the thresholds we have set as the
# maximum possible hunger, boredom and sleepiness

###----Task 4----####
# Make a new method called check_death() that checks when a pet dies.
# These are the conditions I have chosen to use to determine if the pet should be dead.
# (Note: you can change these to make your pet harder or easier to keep alive)
    # ● Boredom is at 10
    # ● Sleepiness is at 10
    # ● Hunger is at 10
    # ● Age is at a random age between 15 and 20 or more


####---Task 5----####
#make it so that the feed, sleep, play and wait will check if the pet
#is dead before you upadate those properties.

####---Task 6----####
#Use Python's predefined __str__ method to produce a string output
#for your pet. refer to page 4 of the tutorial if you don't know
#what I'm talking about.

#Go to page 9 of the tutorial to learn how to make the mainline (https://classroom.google.com/w/NzE2NTQ0NzA2MTYx/t/all)