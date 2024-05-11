class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __repr__(self):
        return f"Country('{self.name}', {self.population})"

    def add(self, other_country):
        combined_name = f"{self.name} {other_country.name}"
        combined_population = self.population + other_country.population
        return Country(combined_name, combined_population)

    def __add__(self, other_country):
        if not isinstance(other_country, Country):
            raise ValueError("Can only add another Country object.")
        combined_name = f"{self.name} {other_country.name}"
        combined_population = self.population + other_country.population
        return Country(combined_name, combined_population)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)

bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)


class Motorcycle:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 299

    def brake(self):
        self.speed -= 299
        if self.speed < 0:
            self.speed = 0

    def display_speed(self):
        print(f"The current speed of the {self.year} {self.brand} {self.model} is {self.speed} km/h.")


my_moto = Motorcycle("Kawasaki", "Ninja", 2022)
my_moto.accelerate()
my_moto.display_speed()
my_moto.brake()
my_moto.display_speed()
