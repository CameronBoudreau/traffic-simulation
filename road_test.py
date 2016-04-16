from Roadrage import *

road = Road()

car1 = Car([60,0])
car2 = Car([75,0], speed=32)
car3 = Car([1000,0])
car4 = Car([68,0], speed=5)
car5 = Car([59,0])
car6 = Car([500,0])
car7 = Car([300,0])
car8 = Car([120,0])
car9 = Car([995,0])

car_list = [car1, car2, car3]
sim = Sim()

def test_reset_car_position_on_loop():
	car3.move_car()
	road.road_loop(car_list, car3, car1)
	assert car_list[0].position[0] == 10

def test_check_car_values():

	assert car1.length == 5
	assert car1.position == [60,0]
	assert car1.max_speed == 33.3
	assert car1.speed == 10
	assert car1.accel == 2
	assert car1.bumper == 55


def test_road_value():
	assert road.length == 1000

def test_car_creater():
	assert len(sim.create_cars()) == 30

	car_set = set([i.position[0] for i in sim.create_cars()])

	assert len(car_set) == 30

def test_change_speed():
	car2.change_speed()
	assert car2.speed == 33.3

def test_collision_check():
	car1.collision_check(car2)
	assert car1.speed == 10

	car1.collision_check(car4)
	assert car1.speed == 5

	car1.collision_check(car5)
	assert car1.speed == 0

def test_check_move_car():
	car6.move_car()
	assert car6.position == [510, 1]

def find_next_car():
	car_list = [car10, car11, car12]

	assert find_next_car(car10, car_list) == car11
	assert find_next_car(car11, car_list) == car12
	assert find_next_car(car12, car_list) == car10

def test_update_positions():
	car13 = Car([1,0], speed=3)
	car14 = Car([450,0], speed=32)
	car15 = Car([995,0])
	""" Have to change the append methods to look for = 2, not 29 since there are only 3 in this list """
	sim.car_list = [car13, car14, car15]
	sim.update_positions(road)
	assert sim.car_position_list == [[4,1], [482, 1], [1000, 1]]
	assert sim.car_speed_list == [5, 33.3, 0]



# def test_update_positions():
# 	car_list = [car7, car8, car9]
# 	sim.update_car_positions(road)
# 	assert car6.positions
