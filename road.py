class Road():
	def __init__(self, length=1000, curve=0):
		self.length = length
		self.curve = curve

	def road_loop(self, car_list, car, next_car):
		if next_car.position[0] - 5 < 6:
			car.position[0] = 1000
			car.speed = 0
		else:
			car.position[0] -= 1000
			car_list.insert(0, car_list.pop())
			car.collision_check(next_car)
		return car_list
