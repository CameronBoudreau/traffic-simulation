from Roadrage_sim_class import *
from Roadrage_road_class import *
from Roadrage_car_class import *

def main():
    sim = Sim()
    road = Road()
    position_matrix = []
    car_list = []

    sim.car_list = sim.create_cars()
    # print("Len of car list: ", len(sim.car_list))
    for car in sim.car_list:
        print(car.position)

    for i in range(1,4):
        print("\n\nRun: ", i)
        position_matrix.append(sim.update_positions(road, sim.car_list))
        # print("This round's matrix addition: ", position_matrix[i-1][:3])
        # print("car_list: ", car_list[:2])

    print("\nFirst round's matrix addition: ", position_matrix[0])
    print("\nSecond round's matrix addition: ", position_matrix[1])
    print("\nThird round's matrix addition: ", position_matrix[2])



if __name__ == '__main__':
    main()
