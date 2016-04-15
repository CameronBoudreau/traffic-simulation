from Roadrage import *

road = Road()

car1 = Car([50,0])
car2 = Car([75,0], speed=32)
car3 = Car([1000,0])

car_list = [car1, car2, car3]
car_list = road.loop(car_list, car3)

sim = Sim()

def test_reset_car_position_on_loop():
	# print("road.loop(car_list)[0].position: ", road.loop(car_list)[0].position)
	assert	car_list[0].position[0] == 0

def test_check_car_values():

	assert car1.length == 5
	assert car1.position == [50,0]
	assert car1.max_speed == 33.3
	assert car1.speed == 10
	assert car1.accel == 2
	assert car1.bumper == 45


def test_road_value():
	assert road.length == 1000

def test_car_creater():
	assert len(sim.create_cars()) == 30

	car_set = set([i.position[0] for i in sim.create_cars()])

	assert len(car_set) == 30


def test_change_speed():
	car2.change_speed()
	assert car2.speed == 33.3
