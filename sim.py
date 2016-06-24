import car


class Sim():
	def __init__(self):
		self.num_of_cars = 30
		self.car_list = []
		self.car_position_list = []
		self.car_speed_list = []

	def __str__():
		print("Runs the simulation.")

	def create_cars(self, max_speed):
		self.car_list = [car.Car([i * 32 + 1, 1], i+1, max_speed=max_speed) for i in range(self.num_of_cars)]
		return self.car_list

	def update_positions(self, road):
		self.car_position_list = []
		for i, car in enumerate(self.car_list):
			self.next_car = self.find_next_car(car, self.car_list, i)
			car.move_car()
			if car == self.car_list[-1]:
				if car.needs_road_loop():
					self.car_list = road.road_loop(self.car_list, car, self.next_car)
				else:
					car.change_speed()
			else:
				car.change_speed()
				car.position = car.collision_check(self.next_car)
		self.car_speed_list = [car.speed for car in self.car_list]
		self.car_position_list = [car.position for car in self.car_list]

	def find_next_car(self, car, car_list, i):
		if car != self.car_list[-1]:
			next_car = self.car_list[i+1]
		else:
			next_car = self.car_list[0]
		return next_car
