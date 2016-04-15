class Road():
	def __init__(self, length = 1000,curve = 0):
		self.length = length
		self.curve = curve

	def loop(self, car_list):

		if car_list[-1].position[0] >= self.length:
			car_list[-1].position[0] = 0

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

	def collision_check(self, next_car):
		difference = next_car.rear_bumper[0] - self.position[0]
		if difference < speed:
			if difference < 0:
				self.position[0] = next_car.rear_bumper[0] - 2
				self.speed = 0
			else:
				self.speed = next_car.speed

	def change_position(self):
		self.position


	def move_car(self, car_list):
		self.change_position()
		self.collision_check()


class Sim():
	def __init__(self):
		self.num_of_cars = 30
		self.car_list = []

	def create_cars(self):
		car_list = [Car([i * 30, 0]) for i in range(self.num_of_cars)]
		return car_list

	def update_positions(self):
		for car in self.car_list[:-2]:
			car.move_car(car+1)
		pass
