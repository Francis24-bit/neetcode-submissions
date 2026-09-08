class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # find the nearest car to the destination: sort
        # zip and sort

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