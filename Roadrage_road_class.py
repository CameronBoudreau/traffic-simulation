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
			# print("Car list in road loop else before pop: ", car_list[0].position, car_list[1].position, car_list[2].position)
			car_list.insert(0,car_list.pop())
			# print("Car list in road loop else after pop: ", car_list[0].position, car_list[1].position, car_list[2].position)
			car.change_speed()
			car.collision_check(next_car)
		return car_list
