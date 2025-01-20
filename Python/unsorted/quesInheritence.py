class Animal:
    def __init__(self, name, sound):
        self.name=name
        self.sound=sound
    def soundMade(self):
        print(f"{self.name} makes {self.sound} sound")
class Dog(Animal):
    def dogSound(self):
        print(f"Dog makes {self.sound} sound")
animal1= Animal ("Shivam", "huhahe")
animal1.soundMade()

dog1=Dog("Raju","bark")
dog1.dogSound()