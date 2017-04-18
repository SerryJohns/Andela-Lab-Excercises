class Car(object):
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

    def drive(self, speed):
        self.speed += speed
        return Car



