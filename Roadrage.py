import random

class Road():
	def __init__(self, length = 1000,curve = 0):
		self.length = length
		self.curve = curve

	def road_loop(self, car_list, car, next_car):
		car.position[0] = (car.position[0] - 1000)

		car_list.insert(0,car_list.pop())
		return car_list

class Car():
	def __init__(self, position, max_speed = 33.3, length = 5, speed = 10):
		self.length = length
		self.position = position
		self.rear_position = self.position[0] - 5
		self.max_speed = max_speed
		self.speed = speed
		self.accel = 2

	# def check_car_distance(self, car_list):
	# 	for car in car_list:
	# 		if self.position[0] == self.position[1]:
	# 			pass

	def change_speed(self):
		if random.randint(1,10) == 7:
			self.speed -= self.accel
		elif self.speed + self.accel > self.max_speed:
			self.speed = self.max_speed
		else:
			self.speed += self.accel		


	def collision_check(self, next_car):
		difference = next_car.bumper[0] - self.position[0]
		if difference < self.speed:
			if difference - self.speed <= 0:
				self.position[0] = next_car.rear_bumper[0] - 2
				self.speed = 0
			else:
				self.speed = next_car.speed

	# def change_position(self, road):
	# 	if self.position[0] + self.speed > 1000:

	# 	else:
	# 		self.position[0] += self.speed

	def move_car(self):
		self.position[0] += self.speed
		self.position[1] +=  1

	def needs_road_loop(self):
		if self.position[0] > 1000: 
			return True


class Sim():
	def __init__(self):
		self.num_of_cars = 30
		self.car_list = []

	def create_cars(self):
		self.car_list = [Car([i * 30, 0]) for i in range(self.num_of_cars)]
		return self.car_list

	def update_positions(self, road):
		for car in self.car_list:
			car.move_car()
			car.change_speed()
			if car.needs_road_loop():
				road.road_loop(car)
			car.collision_check(car_list[car+1])
		pass

