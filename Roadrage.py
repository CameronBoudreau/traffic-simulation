import random
class Road():
	def __init__(self, length = 1000,curve = 0):
		self.length = length
		self.curve = curve

	def road_loop(self , car_list, car, next_car):
		if next_car.bumper < 6:
			car.position[0] = 1000
			car.speed = 0
		else:
			car.position[0] -= 1000
			car_list.insert(0,car_list.pop())
		return car_list

class Car():
	def __init__(self, position, max_speed = 33.3, length = 5, speed = 10):
		self.length = length
		self.position = position

		self.bumper = self.position[0] - 5
		self.max_speed = max_speed
		self.speed = speed
		self.accel = 2


	def __str__(self):
		"I'm at position {}".format(self.position)


	def change_speed(self):
		# if random.randint(1,10) == 7:
		# 	self.speed -= self.accel
		if self.speed + self.accel > self.max_speed:
			self.speed = self.max_speed
		else:
			self.speed += self.accel

	def collision_check(self, next_car):
		difference = next_car.bumper - self.position[0]
		if difference < self.speed:
			if difference <= 0:
				self.position[0] = next_car.bumper - 2
				self.speed = 0
			else:
				self.speed = next_car.speed
		return self.position


	def move_car(self):
		self.position[0] += self.speed
		self.position[1] +=  1
		return self.position

	def needs_road_loop(self):
		if self.position[0] > 1000:
			return True

class Sim():
	def __init__(self):
		self.num_of_cars = 30
		self.car_list = []
		self.car_position_list = []


	def __str__():
		print("Runs the simulation.")

	def create_cars(self):
		self.car_list = [Car([i * 30, 0]) for i in range(self.num_of_cars)]
		return self.car_list

	def update_positions(self, road):
		for i, car in enumerate(self.car_list):
			self.next_car = self.find_next_car(car, self.car_list, i)
			car.move_car()
			if car.needs_road_loop():
				road.road_loop(self.car_list, car, self.next_car)
			else:
				car.position = car.collision_check(self.next_car)
			car.change_speed()
			self.car_position_list.append(car.position)
		return self.car_position_list


	def find_next_car(self, car, car_list, i):
		if car != self.car_list[-1]:
			next_car = self.car_list[i+1]
		else:
			next_car = self.car_list[0]
		return next_car
