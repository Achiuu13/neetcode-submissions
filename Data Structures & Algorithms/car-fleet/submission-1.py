class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        prev = 0
        res = 0
        cars = sorted(zip(position, speed), reverse=True)

        for pos, speed in cars:
            time = (target - pos) / speed
            if time > prev:
                res += 1
                prev = time
        return res