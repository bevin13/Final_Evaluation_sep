class Pet:
    speciesList = ['dog', 'cat', 'horse', 'hamster']

    def __init__(self, species, name):
        if species.lower() not in self.speciesList:
            raise Exception
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        returnValue = "Species of:" + self.species
        if len(name) > 0:
            returnValue = returnValue + "named " + self.name
            return returnValue
        else:
            returnValue = returnValue + "unnamed"
            return returnValue

class Dog(Pet):

    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return self.chases_cats

    def __str__(self):
        returnValue = "Species of Dog = "
        if len(name) > 0:
            returnValue = returnValue + "named " + self.name
            return returnValue
        else:
            returnValue = returnValue + "unnamed"
            return returnValue

  #      returnValue = returnValue + "Chases" + self.chases
   #     return returnValue

class Cat(Pet):

    def __init__(self, name, hates_dogs):
        Pet.__init__(self, name, "Cat")
        self.hates_dogs = hates_dogs

    def hatesDogs(self):
        return self.hates_dogs

    def __str__(self):
        returnValue = "Species of Cat = "
        if len(name) > 0:
            returnValue = returnValue + "named " + self.name
            return returnValue
        else:
            returnValue = returnValue + "unnamed"
            return returnValue

#        returnValue = returnValue + "Hates" + self.hates
 #       return returnValue

if __name__ == '__main__':
    d = {"Dog": [], "Cat": []}

    for i in range(5):
        p = input(print("Enter the name of dogs : "))
        d["Dog"].append(Dog("Dog " + p))
    for i in range(3):
        q = input(print("Enter the name of cats : "))
        d["Cat"].append(Cat("Cat " + q))

