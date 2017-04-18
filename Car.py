import math


class Car():
    def __init__(self, name="General", model="GM", type=""):
        self.type = type
        self.model = model
        self.name = name
        self.speed = 0

        if self.type == "Porshe" or self.type == "Koenigsegg":
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if self.type == "trailer":
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

    def is_saloon(self):
        if self.type == "trailer":
            return False
        else:
            return True

    def drive(self, my_speed):
        if self.type == "trailer":
            self.speed = (11 * my_speed)
        else:
            self.speed = math.ceil((33.33 * my_speed))
        return self
