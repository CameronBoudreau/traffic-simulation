import random


class Car():
    def __init__(self, position, car_id=0, max_speed=33, length=5, speed=10):
        self.length = length
        self.position = position
        self.car_id = car_id
        self.bumper = self.position[0] - 5
        self.max_speed = max_speed
        self.speed = speed
        self.accel = 2

    def __str__(self):
        "I'm car #{}, at position {}".format(self.car_id, self.position)

    def change_speed(self):
        if random.randint(1, 10) == 7 and self.speed != 0:
            self.speed -= self.accel
        elif self.speed + self.accel > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed += self.accel

    def collision_check(self, next_car):
        difference = (next_car.position[0] - 5) - self.position[0]
        if difference < self.speed:
            if difference <= 0:
                self.position[0] = next_car.position[0] - 7
                self.speed = 0
            else:
                self.speed = next_car.speed
        return self.position

    def move_car(self):
        self.position[0] += self.speed
        self.position[1] += 1
        return self.position

    def needs_road_loop(self):
        if self.position[0] > 1000:
            return True
