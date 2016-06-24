import matplotlib.pyplot as plt
import statistics as st
import numpy as np

import road as road_sim
import sim as simulation


def main():
    # Instantiate road and sim classes
    sim = simulation.Sim()
    road = road_sim.Road()

    varied_max_speed_position_dict = {}
    varied_max_speed_speed_dict = {}

    means_plus_devs = []

    # Tests speed limits from 24 to 44 M/S
    for idx in range(12, 22):
        master_list = []
        master_speed_list = []
        limit = idx*2

        # Create the cars on the road
        sim.create_cars(limit)

        start_list = []

        # Setup the initial positions of the cars
        for i in sim.car_list:
            start_list.append(i.position)

        # Creates a list that will hold lists of the cars' positions after each
        # move.
        master_list.append(np.array(start_list))

        # Moves once per second (represented as the y axis on graphs)
        for sec in range(60):
            sim.update_positions(road)
            master_list.append(np.copy(sim.car_position_list))
            master_speed_list.append(np.copy(sim.car_speed_list))

        # Creates a list for each x and y position of the cars for plotting.
        all_xs = []
        all_ys = []

        for second in master_list:
            for position in second:
                all_xs.append(position[0])

        for second in master_list:
            for position in second:
                all_ys.append(position[1])

        # Creates the graph of positions
        plt.plot(all_xs, all_ys, 'ro')
        plt.ylabel("Time")
        plt.xlabel("Position")
        plt.title("Speed Limit {}".format(idx*2))
        plt.axis([0, 1000, 0, 61])
        plt.show()

        all_speeds = []

        for second in master_speed_list:
            for speed in second:
                all_speeds.append(speed)

        mean = st.mean(all_speeds)
        stdev = st.stdev(all_speeds)

        means_plus_devs.append(mean + stdev)

        # Creates a box plot to show standard deviation or how much traffic is
        # having to change speed.
        plt.boxplot(all_speeds, 0, '+')
        plt.ylabel("Speed")
        plt.title("At {} M/S max speed\n********************\nMean: {}\nStandard Deviation: {}\nMean+ 1 Stdev: {}".format((idx*2), mean, stdev, mean + stdev))
        plt.show()
        print()
        varied_max_speed_speed_dict[limit] = master_speed_list
        varied_max_speed_position_dict[limit] = master_list

    # Calculates the average speed plus one standard deviation.
    mean_speed = round(3.6 * st.mean(means_plus_devs))

    print("\n************************************************\n")
    print("That means {} km/h is the best speed limit!".format(mean_speed))
    print("\n************************************************\n")

if __name__ == '__main__':
    main()
