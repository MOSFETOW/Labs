class Humanity:
    def __init__(self, population):
        self._population = population  # protected атрибут

    def grow(self, amount):
        if amount > 0:
            self._population += amount

    def get_population(self):
        return self._population

    def info(self):
        return "Humanity is developing."


class Person(Humanity):
    def __init__(self, name, age, population):
        super().__init__(population)
        self.__name = name      # private атрибут (інкапсуляція)
        self.age = age

    def get_name(self):
        return self.__name

    # Поліморфізм (перевизначення методу)
    def info(self):
        return f"{self.__name} is a part of humanity."
    

#Інкапсуляція — це приховування внутрішніх даних класу та надання доступу до них через спеціальні методи.
#Поліморфізм — це можливість використовувати один і той самий метод по-різному в різних класах.
# Використання
#super() — це вбудована функція в Python, яка дозволяє звертатися до методів батьківського класу з дочірнього. 
if __name__ == "__main__":

    Humanity(8000000000).grow(1000)

    print(Humanity(8000000000).info())
    print(Person("Ivan", 25, 8000000000).info())

    print("Population:", Person("Ivan", 25, 8000000000).get_population())
