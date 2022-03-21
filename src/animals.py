class Animal:
    def __init__(self, age = None, sex = None):
        self.age = age
        self.sex = sex
    
    def eat(self):
        print(f"Animal at age {self.age} is eating")

class Zebra(Animal):
    def __init__(self, number_of_stripes = None, **kwargs):
        super(Zebra, self).__init__(**kwargs)
        self.number_of_stripes = number_of_stripes

    def run_with_herd(self, distance):
        print(f'Zebra is running {distance} km with herd')

def main():
    animal_obj = Animal(age = 2, sex = 'female')
    #print(type(animal_obj))
    #animal_obj.eat()

    zebra_obj = Zebra(number_of_stripes = 42, age = 5, sex = 'male')
    zebra_obj.run_with_herd(5)
    zebra_obj.eat()

if __name__ == '__main__':
    main()
