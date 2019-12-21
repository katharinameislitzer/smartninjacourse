# Read the 2 exercises.
#
# Part 1)
# add 2 methods to the class Car:
# a) decrease energy, this method decreases the battery status by 1
# b) increase energy, this method increases the battery status by 1
# Part 2)
# create an instance of Car
# demonstrate the functioning of the methods
# by always printing the battery status after applying the methods

class Car(object):
    def __init__(self):
        self.energy_status = 100

    def decrease_energy(self):
        self.energy_status -= 1

    def increase_energy(self):
        self.energy_status += 1

ford = Car()
print(ford.energy_status)
ford.decrease_energy()
print(ford.energy_status)
ford.increase_energy()
print(ford.energy_status)

