class Vehicle:
    def __init__(self, model,make):
        self.model = model
        self.make = make

    def move(self):
        print("The vehicle is moving")

class Bus (Vehicle):
    def __init__(self, model, make, capacity):
        super().__init__(model, make)
        self.capacity = capacity

    def hoot (self):
        print("The bus is hooting")

    def check_capacity(self):
        print(f"The capacity is {self.capacity}")


b = Bus("x", "Isuzu", 70)
# b.make()
b.hoot()

class Lorry(Vehicle):
    def __init__(self, model, make, load_weight):
        super().__init__(model, make)
        self.load_weight = load_weight
    def unload(self):
        print("Unloading the lorry")


L = Lorry("T", "mercedes", 1000)
# L.make()
L.unload()

#POLYMORPHISM
class Animal:
    def __init__(self, name):
        self.name = name 

    def move (self):
        pass

    def make_noise(self):
        pass

class Cat (Animal):
    def move(self):
        # return super().move()  
        print("The cat is walking") 
    
    def make_noise(self):
        # return super().make_noise()
        print("meowww")

cat = Cat("cat")
cat.make_noise()

class Bird(Animal):
    def move(self):
        # return super().move()
        print("The bird is flying")

    def make_noise(self):
        # return super().make_noise()
        print("chirp")

bird = Bird("bird")
bird.make_noise()


class Fish(Animal):
    def move(self):
        print("The fish is swimming")

    def make_noise(self):
        # return super().make_noise()
        print("boops")

fish = Fish("fish")
fish.make_noise()