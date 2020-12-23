class House:
    def __init__(self, numGarages, dogName):
        self.numBedrooms = 4
        self.numBaths = 3
        self.numLivingRooms = 1
        self.numBackYard = 1
        self.garageCount = numGarages
        self.nameOfOwner = dogName
        self.solarPanels = 0

    def addSolarPower(self, amount):
        self.solarPanels += amount
        return self

    def changeDogName(self, newName):
        self.nameOfOwner = newName
        return self


#creating instances of house class(house objects)
house1 = House(2, "Junior")
house2 = House(0, "Jeff")
house3 = House(1, "Rover")
house4 = House(2, "Beamer")


print(house1.solarPanels)
print(house2.solarPanels)
print(house3.solarPanels)
print(house4.solarPanels)

print("*********")
house1.addSolarPower(3).addSolarPower(5).addSolarPower(10).changeDogName("WoofWoof").addSolarPower(5)
house2.addSolarPower(2).changeDogName("RuffRuff")
house3.addSolarPower(5).addSolarPower(-2).changeDogName("Dog died")

print("House #1 features:")
print("------------------")
print("Bedrooms(s):", house1.numBedrooms)
print("Bathroom(s):", house1.numBaths )
print("Living room(s):", house1.numLivingRooms)
print("Backyard(s):", house1.numBackYard)
print("Garage(s):", house1.garageCount)
print("Dog name: ", house1.nameOfOwner)
print("Solar Panel(s):", house1.solarPanels)

# print(house1.solarPanels)
# print(house2.solarPanels)
# print(house3.solarPanels)
# print(house4.solarPanels)
# print(house1.nameOfOwner)