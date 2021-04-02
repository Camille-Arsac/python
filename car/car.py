class Car:
    def __init__(self,
                 max_speed,
                 fuel_consumption,
                 seats):
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0
        self.fuel_consumption = fuel_consumption
        self.current_fuel = 0
        self.seats = seats
        self.person_in_car = []

    def add_in_car(self, person):
        if len(self.person_in_car) < self.seats:
            self.person_in_car.append(person)

    def remove_in_car(self, person):
        if person in self.person_in_car:
            self.person_in_car.remove(person)

    def advance(self, speed, time):
        self.current_fuel -= self.fuel_consumption
        self.distance += speed
        time -= 1
