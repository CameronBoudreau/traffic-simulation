class Road():
	def __init__(self, length = 1000,curve = 0):
		self.length = length
		self.curve = curve
	
	def loop(self, car_list):
		
		if car_list[-1].frontofcar[0] >= self.length:
			car_list[-1].frontofcar[0] = 0 

		car_list.insert(0,car_list.pop())
		return car_list

class Car():
	def __init__(self, frontofcar, max_speed = 33.3, length = 5,):
		self.length = length
		self.frontofcar = frontofcar
		self.max_speed = max_speed
		self.speed = 0
		self.accel = 2

	def check_car_distance(self, car_list):
		for car in car_list:
			if self.frontofcar[0] == self.frontofcar[1]:
				pass


class Sim():
	def __init__(self):
		self.num_of_cars = 30

	def create_cars(self):
		cars = []