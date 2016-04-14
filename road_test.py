from Roadrage import *

road = Road()

car1 = Car([50,0])
car2 = Car([75,0])
car3 = Car([1000,0])

car_list = [car1, car2, car3]
car_list = road.loop(car_list)
def test_reset_car_position_on_loop():
	# print("road.loop(car_list)[0].frontofcar: ", road.loop(car_list)[0].frontofcar)
	assert	car_list[0].frontofcar[0] == 0

def test_check_car_values():

	assert car1.length == 5
	assert car1.frontofcar == [50,0]
	assert car1.max_speed == 33.3
	assert car1.speed == 0
	assert car1.accel == 2


def test_road_value():
	assert road.length == 1000

# def car_has_a_length():
# 	pass

# def car_has_a():
# 	pass