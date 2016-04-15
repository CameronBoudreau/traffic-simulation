import random

class Road():
	def __init__(self, length = 1000,curve = 0):
		self.length = length
		self.curve = curve

	def loop(self, car):
		self.position[0] = (self.position[0] - 1000)

		car_list.insert(0,car_list.pop())
		return car_list

class Car():
	def __init__(self, position, max_speed = 33.3, length = 5, speed = 10):
		self.length = length
		self.position = position
		self.rear_rear_position = self.position[0] - 5
		self.max_speed = max_speed
		self.speed = speed
		self.accel = 2

	# def check_car_distance(self, car_list):
	# 	for car in car_list:
	# 		if self.position[0] == self.position[1]:
	# 			pass

	def decelerate(self):
		if random.randint(1,10)== 7:
			return True



	def collision_check(self, next_car):
		difference = next_car.rear_bumper[0] - self.position[0]
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
		if decelerate():
			self.speed -= self.accel
		else:
			self.speed += self.accel
		# if self.needs_loop():
		# 	return True
		# self.change_position()
		# self.collision_check()
		# if self.will_slow():
		# 	self.speed -= 2

	def needs_loop(self):
		if self.position[0] > 1000: 
			return True


class Sim():
	def __init__(self):
		self.num_of_cars = 30
		self.car_list = []

	def create_cars(self):
		car_list = [Car([i * 30, 0]) for i in range(self.num_of_cars)]
		return car_list

	def update_positions(self, road):
		for car in self.car_list:
			car.move_car()
			if self.needs_loop(car):
				road.loop(car)
			car.collision_check(car_list[car+1])
		pass

x = Sim()
