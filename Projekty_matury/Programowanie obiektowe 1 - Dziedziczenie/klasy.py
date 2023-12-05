class Animal:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def speak(self):
        print("WTF!!")

    def introducing(self):
        print(f"I am a {self.name} and I am {self.age} years old")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def introducing(self):
        print(f"I am a {self.name} and I am {self.age} years old and I am {self.color}")
        
