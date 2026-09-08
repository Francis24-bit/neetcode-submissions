class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # this problem asks how many fleet can arrive at the destination at the same time(as when you catch up, you can only travel as fast as the car before you)

        # in other words, a fleet in code is represented as the time at which one car or several cars arrive at the destination.

        # so we start with the nearest car to the destinaiton(zip the speed and position, and sort), figure out its time to arrive, and look at the arrive time of the car behind it.

        # if the car behind travels faster, it can only arrive at the target with the car before it(per rule), in this case, they are in one group.

        # the key is to understand that different fleets are actually different time that cars arrive.

        cars = list(zip(position, speed))
        cars.sort(reverse = True)

        count = 1
        current_time = (target - cars[0][0]) / cars[0][1]

        for i in range(1, len(cars)):
            new_time = (target - cars[i][0]) / cars[i][1]
        
            if new_time > current_time:
                count += 1
                current_time = new_time
        
        return count