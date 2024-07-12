import random
from collections import deque

class Plane:
    def __init__(self, id, event_time):
        self.id = id
        self.event_time = event_time

def simulate_airport(num_planes, landing_time, takeoff_time):
    arrival_queue = deque()
    departure_queue = deque()
    runway_free = True
    time = 0
    total_arrival_wait_time = 0
    total_departure_wait_time = 0
    num_arrivals = 0
    num_departures = 0
    max_arrival_queue_length = 0
    max_departure_queue_length = 0

    while num_arrivals + num_departures < num_planes:
        # Plane arrival event
        if random.random() < 0.5 and num_arrivals < num_planes:
            new_plane = Plane(num_arrivals + 1, time)
            if runway_free:
                runway_free = False
                current_time = plane_lands(time, new_plane, landing_time)
                total_arrival_wait_time += 0
                num_arrivals += 1
            else:
                arrival_queue.append(new_plane)
                max_arrival_queue_length = max(max_arrival_queue_length, len(arrival_queue))

        # Plane departure event
        if random.random() < 0.5 and num_departures < num_planes:
            new_plane = Plane(num_departures + 1, time)
            if runway_free and not arrival_queue:
                runway_free = False
                current_time = plane_takes_off(time, new_plane, takeoff_time)
                total_departure_wait_time += 0
                num_departures += 1
            else:
                departure_queue.append(new_plane)
                max_departure_queue_length = max(max_departure_queue_length, len(departure_queue))

        # Runway availability check
        if not runway_free:
            runway_free = check_runway(time, arrival_queue, departure_queue, 
                                       total_arrival_wait_time, total_departure_wait_time, 
                                       num_arrivals, num_departures, landing_time, takeoff_time)

        time += 1

    print_simulation_results(num_arrivals, total_arrival_wait_time, num_departures, total_departure_wait_time,
                             max_arrival_queue_length, max_departure_queue_length)

def plane_lands(current_time, plane, landing_time):
    print(f"Plane {plane.id} lands at time {current_time}")
    for _ in range(landing_time):
        current_time += 1  # Simulate the time it takes to land
    return current_time

def plane_takes_off(current_time, plane, takeoff_time):
    print(f"Plane {plane.id} takes off at time {current_time}")
    for _ in range(takeoff_time):
        current_time += 1  # Simulate the time it takes to take off
    return current_time

def check_runway(current_time, arrival_queue, departure_queue, 
                 total_arrival_wait_time, total_departure_wait_time, 
                 num_arrivals, num_departures, landing_time, takeoff_time):
    if arrival_queue:
        plane = arrival_queue.popleft()
        total_arrival_wait_time += current_time - plane.event_time
        num_arrivals += 1
        current_time = plane_lands(current_time, plane, landing_time)
        return False
    elif departure_queue and not arrival_queue:
        plane = departure_queue.popleft()
        total_departure_wait_time += current_time - plane.event_time
        num_departures += 1
        current_time = plane_takes_off(current_time, plane, takeoff_time)
        return False
    return True

def print_simulation_results(num_arrivals, total_arrival_wait_time, num_departures, total_departure_wait_time,
                             max_arrival_queue_length, max_departure_queue_length):
    avg_arrival_wait_time = total_arrival_wait_time / num_arrivals if num_arrivals else 0
    avg_departure_wait_time = total_departure_wait_time / num_departures if num_departures else 0
    print(f"\nSimulation Results:")
    print(f"Average wait time for arrivals: {avg_arrival_wait_time:.2f} time units")
    print(f"Average wait time for departures: {avg_departure_wait_time:.2f} time units")
    print(f"Maximum number of planes in arrival queue: {max_arrival_queue_length}")
    print(f"Maximum number of planes in departure queue: {max_departure_queue_length}")

# Get user input for the simulation parameters
num_planes = int(input("Enter the number of planes to simulate: "))
landing_time = int(input("Enter the time it takes for a plane to land (in time units): "))
takeoff_time = int(input("Enter the time it takes for a plane to take off (in time units): "))

simulate_airport(num_planes, landing_time, takeoff_time)