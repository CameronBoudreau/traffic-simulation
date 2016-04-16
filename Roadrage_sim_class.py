from Roadrage_car_class import *

class Sim():
	def __init__(self):
		self.num_of_cars = 5
		self.car_list = []
		self.car_position_list = []
		self.car_speed_list = []


	def __str__():
		print("Runs the simulation.")

	def create_cars(self):
		self.car_list = [Car([i * 30, 0]) for i in range(self.num_of_cars)]
		return self.car_list

	def update_positions(self, road, car_list):
		for i, car in enumerate(self.car_list):
			# print("Run: ", i+1)
			self.next_car = self.find_next_car(car, self.car_list, i)
			car.move_car()
			if car.needs_road_loop():
				road.road_loop(self.car_list, car, self.next_car)
				# print("Car list after road loop: ", self.car_list[0].position, self.car_list[1].position, self.car_list[2].position)
			else:
				car.change_speed()
				car.position = car.collision_check(self.next_car)
			self.add_to_position_list(car, i)
			# print("Car position list: ", self.car_position_list)
			self.add_to_speed_list(car, i)
		print("Car position list: ", self.car_position_list)
		return self.car_position_list


	def add_to_position_list(self, car, i):
		if i == 2:
			self.car_position_list.insert(0, car.position)
		else:
			self.car_position_list.append(car.position)


	def add_to_speed_list(self, car, i):
		if i == 2:
			self.car_speed_list.insert(0, car.speed)
		else:
			self.car_speed_list.append(car.speed)


	def find_next_car(self, car, car_list, i):
		if car != self.car_list[-1]:
			next_car = self.car_list[i+1]
		else:
			next_car = self.car_list[0]
		return next_car
