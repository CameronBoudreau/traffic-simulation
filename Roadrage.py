import random
class Road():
	def __init__(self, length = 1000,curve = 0):
		self.length = length
		self.curve = curve

	def road_loop(self , car_list, car, next_car):
		print("Car position: ", car.position)
		if next_car.bumper < 6:
			car.position[0] = 1000
		else:
			car.position[0] = car.position[0] - 1000
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
		print("In collision change car pos: ", self.position)
		print("difference: ", difference)
		if difference < self.speed:
			if difference <= 0:
				self.position[0] = next_car.bumper - 2
				self.speed = 0
			else:
				self.speed = next_car.speed
		print("Last collision change car pos: ", self.position)
		return self.position


	def move_car(self):
		print("Position before move: ", self.position)
		self.position[0] += self.speed
		self.position[1] +=  1
		print("Position after move: ", self.position)
		return self.position

	def needs_road_loop(self):
		if self.position[0] > 1000:
			return True

class Sim():
	def __init__(self):
		self.num_of_cars = 30
		self.car_list = []
		self.car_position_list = []


	def create_cars(self):
		self.car_list = [Car([i * 30, 0]) for i in range(self.num_of_cars)]
		return self.car_list

	def update_positions(self, road):
		for i, car in enumerate(self.car_list):
			print("Run ", i)
			next_car = self.find_next_car(car, self.car_list, i)
			# print("next car: ", str(next_car))
			print("Before move")
			car.move_car()
			print("After move")
			if car.needs_road_loop():
				road.road_loop(self.car_list, car, next_car)
			print("After loop")
			car.change_speed()
			print("After speed change car pos: ", car.position)
			car.position = car.collision_check(next_car)
			print("After speed collision car pos: ", car.position)
			self.car_position_list.append(car.position)

			print("Sim list: ", self.car_position_list)
		return self.car_position_list


	def find_next_car(self, car, car_list, i):
		if car != self.car_list[-1]:
			next_car = self.car_list[i+1]
		else:
			next_car = self.car_list[0]
		print("next car: ", next_car.position)
		return next_car

